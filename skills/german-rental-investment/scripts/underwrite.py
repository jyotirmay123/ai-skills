#!/usr/bin/env python3
"""Conservative, source-dependent German rental acquisition arithmetic.

No web requests, tax advice, forecasts, or decision of BUY. The input must be
independently verified by the calling agent; see ../SKILL.md.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path


YEARS = 10
REPAIR_SHOCK_EUR = 10_000
REFINANCE_SHOCK_PP = 2.0
MIN_SCREEN_DSCR = 1.10


def number(value, name, minimum=None, maximum=None):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name}: expected a number; unknown is not zero")
    v = float(value)
    if not math.isfinite(v):
        raise ValueError(f"{name}: expected a finite number")
    if minimum is not None and v < minimum:
        raise ValueError(f"{name}: must be >= {minimum}")
    if maximum is not None and v > maximum:
        raise ValueError(f"{name}: must be <= {maximum}")
    return v


def field(item, key, parent="", minimum=None, maximum=None):
    if key not in item:
        raise ValueError(f"{parent}{key}: missing, not assumed zero")
    return number(item[key], f"{parent}{key}", minimum, maximum)


def verified(item, key):
    if key not in item:
        raise ValueError(f"{key}: missing, not assumed false")
    if not isinstance(item[key], bool):
        raise ValueError(f"{key}: expected boolean")
    return item[key]


def monthly_payment(balance, annual_rate_pct, repayment_pct, remaining_term=None):
    r = annual_rate_pct / 1200
    if remaining_term is not None:
        if remaining_term <= 0:
            return balance * (1 + r)
        if r == 0:
            return balance / remaining_term
        return balance * r / (1 - (1 + r) ** (-remaining_term))
    return balance * (annual_rate_pct + repayment_pct) / 1200


def loan_schedules(loans, shock=False):
    yearly_service = [0.0] * YEARS
    yearly_interest = [0.0] * YEARS
    yearly_principal = [0.0] * YEARS
    loan_results = []
    for index, loan in enumerate(loans):
        prefix = f"loans[{index}]."
        balance = field(loan, "principal_eur", prefix, minimum=0)
        original = balance
        rate = field(loan, "annual_interest_pct", prefix, minimum=0, maximum=100)
        repay = field(loan, "initial_repayment_pct", prefix, minimum=0, maximum=100)
        fixed_years = field(loan, "fixed_years", prefix, minimum=1)
        if fixed_years != int(fixed_years):
            raise ValueError(f"{prefix}fixed_years must be an integer")
        term = None
        if "term_months" in loan and loan["term_months"] is not None:
            term = int(field(loan, "term_months", prefix, minimum=1))
            if term != loan["term_months"]:
                raise ValueError(f"{prefix}term_months must be an integer")
        if repay <= 0 and term is None and balance > 0:
            raise ValueError(f"{prefix}requires initial repayment or term_months")
        fix_month = int(fixed_years) * 12
        payment = monthly_payment(balance, rate, repay, term)
        initial_payment = payment
        for month in range(1, YEARS * 12 + 1):
            if balance <= 1e-8:
                break
            if month == fix_month + 1 and shock:
                rate += REFINANCE_SHOCK_PP
                remaining = max(1, term - month + 1) if term else None
                payment = monthly_payment(balance, rate, repay, remaining)
            interest = balance * rate / 1200
            paid = min(payment, balance + interest)
            principal_paid = paid - interest
            if principal_paid < -1e-7:
                raise ValueError(f"{prefix}negative amortization")
            balance = max(0.0, balance - principal_paid)
            year = (month - 1) // 12
            yearly_service[year] += paid
            yearly_interest[year] += interest
            yearly_principal[year] += principal_paid
        loan_results.append({
            "original_principal_eur": round(original, 2),
            "initial_monthly_payment_eur": round(initial_payment, 2),
            "balance_after_10y_eur": round(balance, 2),
            "fixed_years": int(fixed_years),
            "refinancing_shocked_inside_horizon": bool(shock and fixed_years < YEARS),
        })
    return {
        "debt_service_by_year_eur": yearly_service,
        "interest_by_year_eur": yearly_interest,
        "principal_by_year_eur": yearly_principal,
        "remaining_balance_eur": sum(x["balance_after_10y_eur"] for x in loan_results),
        "loan_details": loan_results,
    }


def irr(cashflows):
    """Bisection for a conventional (-initial, then annual inflows) cash stream."""
    if cashflows[0] >= 0:
        return None
    def npv(r):
        return sum(v / ((1 + r) ** i) for i, v in enumerate(cashflows))
    low, high = -0.99, 10.0
    if npv(low) * npv(high) > 0:
        return None
    for _ in range(160):
        mid = (low + high) / 2
        if npv(low) * npv(mid) <= 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2


def money(value):
    return round(value, 2) if value is not None else None


def evaluate(data):
    price = field(data, "price_eur", minimum=0.01)
    area = field(data, "area_m2", minimum=0.01)
    costs = field(data, "acquisition_costs_eur", minimum=0)
    market_value = field(data, "market_value_eur", minimum=0.01)
    proposed = field(data, "proposed_rent_cold_month_eur", minimum=0)
    market_rent = field(data, "market_rent_cold_month_eur", minimum=0)
    legal_cap = field(data, "legal_max_rent_cold_month_eur", minimum=0)
    vacancy = field(data, "vacancy_fraction", minimum=0, maximum=1)
    opex = field(data, "nonrecoverable_cost_month_eur", minimum=0)
    maintenance = field(data, "owner_maintenance_month_eur", minimum=0)
    selling_cost = field(data, "sale_cost_fraction", minimum=0, maximum=0.4)
    tax_effect = field(data, "annual_incremental_tax_effect_eur")

    flags = ("listing_verified", "rent_law_verified", "financing_verified",
             "property_docs_verified", "tax_effect_verified")
    lacking_evidence = [flag for flag in flags if not verified(data, flag)]
    for key in ("listing_url", "rent_law_source_url", "rent_law_checked_on", "observed_on"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            lacking_evidence.append(key)

    portfolio = data.get("portfolio")
    if not isinstance(portfolio, dict):
        raise ValueError("portfolio: expected verified property and household baseline")
    pre = "portfolio."
    existing_rent = field(portfolio, "existing_annual_rent_eur", pre, minimum=0)
    existing_noi = field(portfolio, "existing_annual_noi_eur", pre)
    existing_service = field(portfolio, "existing_annual_debt_service_eur", pre, minimum=0)
    existing_cf = field(portfolio, "existing_annual_net_cashflow_eur", pre)
    liquid = field(portfolio, "liquid_after_close_eur", pre, minimum=0)
    cash_floor = field(portfolio, "minimum_cash_floor_eur", pre, minimum=0)
    stress_net_pay = field(portfolio, "salary_net_after_20pct_gross_cut_month_eur", pre, minimum=0)
    essentials = field(portfolio, "household_essentials_month_eur", pre, minimum=0)

    loans = data.get("loans")
    if not isinstance(loans, list) or not loans:
        raise ValueError("loans: required nonempty list; cash acquisitions need explicit modeling")
    total_loan = sum(field(v, "principal_eur", f"loans[{i}].", minimum=0)
                     for i, v in enumerate(loans))
    if total_loan > price + costs + 1e-6:
        raise ValueError("financed principal cannot exceed modeled total uses without an extra use-of-funds schedule")
    upfront_cash = price + costs - total_loan
    base_debt = loan_schedules(loans, shock=False)
    shock_debt = loan_schedules(loans, shock=True)

    annual_rent = 12 * min(market_rent, legal_cap) * (1 - vacancy)
    annual_opex = 12 * (opex + maintenance)
    noi = annual_rent - annual_opex
    base_cf = [noi - service for service in base_debt["debt_service_by_year_eur"]]
    shocked_rent = annual_rent * 0.90
    shocked_noi = shocked_rent - annual_opex
    shock_cf = [shocked_noi - service for service in shock_debt["debt_service_by_year_eur"]]
    portfolio_shock_cf = [existing_cf - 0.10 * existing_rent + value for value in shock_cf]
    worst_portfolio_year = min(portfolio_shock_cf)
    # Reserve floor survives both a dedicated €10k repair and 12 months of the worst
    # stressed rental support need. Existing cash flows must be before tax refunds.
    reserve_required = cash_floor + REPAIR_SHOCK_EUR + max(0.0, -worst_portfolio_year)
    salary_stress_margin = stress_net_pay - essentials + min(0.0, worst_portfolio_year / 12)
    dscr = noi / base_debt["debt_service_by_year_eur"][0] if base_debt["debt_service_by_year_eur"][0] else None
    denom = existing_service + base_debt["debt_service_by_year_eur"][0]
    combined_dscr = (existing_noi + noi) / denom if denom else None

    exits = {}
    for name, annual_change in (("downside_minus_1pct", -0.01), ("zero_growth", 0.0),
                                ("upside_plus_2pct", 0.02)):
        sale = price * ((1 + annual_change) ** YEARS)
        sale_net_before_tax = sale * (1 - selling_cost) - base_debt["remaining_balance_eur"]
        cashflow = [-upfront_cash, *base_cf]
        cashflow[-1] += sale_net_before_tax
        rate = irr(cashflow)
        exits[name] = {
            "sale_price_eur": money(sale),
            "sale_proceeds_after_costs_and_loans_before_tax_eur": money(sale_net_before_tax),
            "nominal_total_gain_before_tax_eur": money(sum(cashflow)),
            "annualized_irr_before_tax_pct": money(100 * rate) if rate is not None else None,
        }

    issues = []
    if proposed > legal_cap + 0.01:
        issues.append("advertised_or_proposed_cold_rent_exceeds_input_legal_cap")
    if base_cf[0] < -0.01:
        issues.append("negative_normalized_first_year_pretax_cashflow")
    if liquid < reserve_required - 0.01:
        issues.append("post_closing_liquid_reserve_fails_stress_floor")
    if salary_stress_margin < -0.01:
        issues.append("gross_salary_cut_recomputed_net_cannot_support_essentials_and_rental_deficit")
    if dscr is not None and dscr < MIN_SCREEN_DSCR:
        issues.append("property_dscr_below_1_10")
    if combined_dscr is not None and combined_dscr < MIN_SCREEN_DSCR:
        issues.append("portfolio_dscr_below_1_10")
    if price > market_value * 1.05:
        issues.append("purchase_price_more_than_5pct_above_independent_value")
    if exits["zero_growth"]["nominal_total_gain_before_tax_eur"] <= 0:
        issues.append("zero_appreciation_10y_pretax_gain_nonpositive")
    if min(shock_cf) < -0.01:
        issues.append("candidate_annual_cashflow_negative_under_rent_and_refixation_shock")

    fundamental = {
        "advertised_or_proposed_cold_rent_exceeds_input_legal_cap",
        "negative_normalized_first_year_pretax_cashflow",
        "post_closing_liquid_reserve_fails_stress_floor",
        "gross_salary_cut_recomputed_net_cannot_support_essentials_and_rental_deficit",
    }
    if any(issue in fundamental for issue in issues):
        decision = "REJECT"
    elif lacking_evidence:
        decision = "INSUFFICIENT_DATA"
    elif issues:
        decision = "NEGOTIATE_OR_WATCH"
    else:
        decision = "PRELIMINARY_SHORTLIST"

    return {
        "decision": decision,
        "never_a_final_buy_approval": True,
        "missing_critical_verifications": lacking_evidence,
        "screening_issues": issues,
        "property": {
            "price_per_m2_eur": money(price / area),
            "all_in_cost_eur": money(price + costs),
            "upfront_cash_eur": money(upfront_cash),
            "legal_monthly_rent_underwritten_eur": money(min(market_rent, legal_cap)),
            "annual_collected_rent_base_eur": money(annual_rent),
            "annual_collected_rent_stress_eur": money(shocked_rent),
            "noi_year1_eur": money(noi),
            "debt_service_year1_eur": money(base_debt["debt_service_by_year_eur"][0]),
            "interest_year1_eur": money(base_debt["interest_by_year_eur"][0]),
            "principal_repaid_year1_eur": money(base_debt["principal_by_year_eur"][0]),
            "cashflow_pretax_year1_eur": money(base_cf[0]),
            "cashflow_after_tax_year1_eur": money(base_cf[0] + tax_effect)
                if data["tax_effect_verified"] else None,
            "dscr_year1": money(dscr),
            "balance_after_10y_eur": money(base_debt["remaining_balance_eur"]),
            "base_cashflow_by_year_eur": [money(x) for x in base_cf],
            "shocked_cashflow_by_year_eur": [money(x) for x in shock_cf],
            "loan_details": base_debt["loan_details"],
        },
        "portfolio": {
            "combined_dscr_year1": money(combined_dscr),
            "worst_stressed_annual_rental_cashflow_eur": money(worst_portfolio_year),
            "required_liquid_reserve_eur": money(reserve_required),
            "liquid_after_closing_eur": money(liquid),
            "liquid_after_one_off_repair_eur": money(liquid - REPAIR_SHOCK_EUR),
            "salary_cut_net_margin_after_essentials_and_deficit_month_eur": money(salary_stress_margin),
        },
        "exit_scenarios": exits,
        "limitations": [
            "Arithmetic screen only; evidence flags are inputs, not independently authenticated",
            "Do not treat the labeled scenarios as likelihoods or probabilities",
            "10-year exit values and IRR are PRE-TAX; sale taxes, early repayment penalties and tax basis need independent review",
            "Constant no-shock interest after fixation is illustrative, not a lender offer",
            "Loan rates are nominal; effective APR and fees require offer-level validation",
            "Guarantees and seller subsidies excluded; underwrite unsupported upside separately",
            "Existing portfolio cashflow must exclude tax refunds and actual debt must be complete",
            "Tax amount is supplied by independent incremental household tax model, not calculated here",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scenario", type=Path, help="Complete, independently verified scenario JSON")
    args = parser.parse_args()
    try:
        with args.scenario.open(encoding="utf-8") as handle:
            data = json.load(handle)
        result = evaluate(data)
    except (OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"decision": "INSUFFICIENT_DATA", "error": str(exc)}), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
