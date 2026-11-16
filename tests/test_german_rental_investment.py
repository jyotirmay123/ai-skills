#!/usr/bin/env python3
"""Offline invariant checks for the rental-investment calculation helper."""
import importlib.util
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "german-rental-investment"
SPEC = importlib.util.spec_from_file_location("underwrite", SKILL / "scripts" / "underwrite.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def fixture():
    return json.loads((SKILL / "examples" / "synthetic-deal.json").read_text(encoding="utf-8"))


class UnderwriteTests(unittest.TestCase):
    def complete(self):
        d = fixture()
        for flag in ("listing_verified", "rent_law_verified", "financing_verified",
                     "property_docs_verified", "tax_effect_verified"):
            d[flag] = True
        return d

    def test_missing_evidence_never_promoted(self):
        result = MODULE.evaluate(fixture())
        self.assertEqual(result["decision"], "INSUFFICIENT_DATA")
        self.assertIsNone(result["property"]["cashflow_after_tax_year1_eur"])

    def test_healthy_synthetic_case_is_shortlist_not_buy(self):
        result = MODULE.evaluate(self.complete())
        self.assertEqual(result["decision"], "PRELIMINARY_SHORTLIST")
        self.assertEqual(result["property"]["cashflow_pretax_year1_eur"], 2880.0)
        self.assertGreater(result["portfolio"]["combined_dscr_year1"], 1.1)
        self.assertTrue(result["never_a_final_buy_approval"])

    def test_illegal_advertised_rent_is_rejected(self):
        d = self.complete()
        d["proposed_rent_cold_month_eur"] = 1600
        result = MODULE.evaluate(d)
        self.assertEqual(result["decision"], "REJECT")
        self.assertEqual(result["property"]["legal_monthly_rent_underwritten_eur"], 1200)

    def test_reserve_gate(self):
        d = self.complete()
        d["portfolio"]["liquid_after_close_eur"] = 38000
        result = MODULE.evaluate(d)
        self.assertEqual(result["decision"], "REJECT")
        self.assertIn("post_closing_liquid_reserve_fails_stress_floor", result["screening_issues"])

    def test_cashflow_loss_not_hidden_by_tax(self):
        d = self.complete()
        d["market_rent_cold_month_eur"] = 550
        d["annual_incremental_tax_effect_eur"] = 15000
        result = MODULE.evaluate(d)
        self.assertEqual(result["decision"], "REJECT")
        self.assertLess(result["property"]["cashflow_pretax_year1_eur"], 0)
        self.assertGreater(result["property"]["cashflow_after_tax_year1_eur"], 0)

    def test_refinance_shock_applies_only_after_fixation(self):
        d = self.complete()
        d["loans"][0]["fixed_years"] = 5
        base = MODULE.loan_schedules(d["loans"], shock=False)
        stress = MODULE.loan_schedules(d["loans"], shock=True)
        self.assertAlmostEqual(base["debt_service_by_year_eur"][0],
                               stress["debt_service_by_year_eur"][0], delta=0.01)
        self.assertGreater(stress["debt_service_by_year_eur"][5],
                           base["debt_service_by_year_eur"][5])

    def test_unknown_not_zero(self):
        d = self.complete()
        del d["portfolio"]["liquid_after_close_eur"]
        with self.assertRaisesRegex(ValueError, "missing"):
            MODULE.evaluate(d)


if __name__ == "__main__":
    unittest.main()
