"""
Question 3: Income tax calculators (Federal + State)

Assumptions (typical for intro assignments):
- Treat the given `income` as *taxable income* (ignore deductions/credits).
- Use progressive brackets for FED, CA, NY.
- MA is a flat 5% tax.
"""

from __future__ import annotations

from typing import List, Tuple


def _progressive_tax(income: int, brackets: List[Tuple[int, float]]) -> float:
    """
    Generic progressive tax calculator.

    brackets: list of (lower_bound, rate) sorted ascending by lower_bound.
    Example:
        [(0, 0.10), (11601, 0.12), ...]
    """
    if income <= 0:
        return 0.0

    # Ensure sorted by threshold
    brackets = sorted(brackets, key=lambda x: x[0])

    tax = 0.0
    for i, (lower, rate) in enumerate(brackets):
        # upper bound is next bracket's lower bound - 1, or infinity for last bracket
        upper = brackets[i + 1][0] if i + 1 < len(brackets) else None

        if income <= lower:
            break

        taxable_in_bracket = (income if upper is None else min(income, upper)) - lower
        tax += taxable_in_bracket * rate

    return float(tax)


def income_tax_fed(income: int) -> float:
    """Calculates US federal income tax (using IRS 2024 single filer brackets)."""
    brackets = [
        (0, 0.10),
        (11600, 0.12),
        (47150, 0.22),
        (100525, 0.24),
        (191950, 0.32),
        (243725, 0.35),
        (609350, 0.37),
    ]
    # Note: We use lower bounds as listed; this version treats thresholds as inclusive starts.
    # Using (11600, 0.12) means first bracket covers [0,11600), which is fine for this assignment style.
    return _progressive_tax(income, brackets)


def income_tax_ca(income: int) -> float:
    """Calculates California state income tax (2024 Schedule X: Single)."""
    brackets = [
        (0, 0.01),
        (10756, 0.02),
        (25499, 0.04),
        (40245, 0.06),
        (55866, 0.08),
        (70606, 0.093),
        (360659, 0.103),
        (432787, 0.113),
        (721314, 0.123),
    ]
    return _progressive_tax(income, brackets)


def income_tax_ma(income: int) -> float:
    """Massachusetts: flat 5%."""
    if income <= 0:
        return 0.0
    return float(income) * 0.05


def income_tax_ny(income: int) -> float:
    """Calculates New York state income tax (typical NYS single brackets)."""
    brackets = [
        (0, 0.04),
        (8500, 0.045),
        (11700, 0.0525),
        (13900, 0.055),
        (80650, 0.06),
        (215400, 0.0685),
        (1077550, 0.0965),
        (5000000, 0.103),
        (25000000, 0.109),
    ]
    return _progressive_tax(income, brackets)


def calculate_income_tax() -> None:
    """
    1. Ask the user to input their state (CA, MA, NY)
    2. Ask the user to input an annual income (int)
    3. Print: "Your income is XX before tax and XX after tax. You pay XX income tax."
       (This prints total income tax = federal + state)
    4. Handle invalid inputs gracefully
    """
    print("Enter your state (CA, MA, NY).")

    state_to_func = {
        "CA": income_tax_ca,
        "MA": income_tax_ma,
        "NY": income_tax_ny,
    }

    while True:
        state = input("State: ").strip().upper()
        if state in state_to_func:
            break
        print("Invalid state. Please enter CA, MA, or NY.")

    while True:
        raw_income = input("Annual income: ").strip()
        try:
            income = int(raw_income)
            if income < 0:
                print("Income must be a non-negative integer.")
                continue
            break
        except ValueError:
            print("Invalid income. Please enter a whole number.")

    fed_tax = income_tax_fed(income)
    state_tax = state_to_func[state](income)
    total_tax = fed_tax + state_tax
    after_tax = income - total_tax

    print(
        f"Your income is {income} before tax and {after_tax} after tax. "
        f"You pay {total_tax} income tax."
    )
