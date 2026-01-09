"""Tests for Lab 1 Question 3"""

import sys
import io
import unittest
from unittest.mock import patch, Mock

sys.path.append(".")

from src.q3 import (
    income_tax_fed,
    income_tax_ca,
    income_tax_ma,
    income_tax_ny,
    calculate_income_tax,
)


class TestIncomeTaxFunctions(unittest.TestCase):
    def test_ma_flat_tax(self) -> None:
        self.assertAlmostEqual(income_tax_ma(0), 0.0)
        self.assertAlmostEqual(income_tax_ma(100), 5.0)
        self.assertAlmostEqual(income_tax_ma(1000), 50.0)

    def test_fed_basic_bracket(self) -> None:
        # For small income entirely in the first bracket, tax should be rate * income
        # (Assuming the function follows the assignment’s progressive bracket logic)
        self.assertAlmostEqual(income_tax_fed(10_000), 1000.0)

    def test_ca_basic_bracket(self) -> None:
        self.assertAlmostEqual(income_tax_ca(10_000), 100.0)

    def test_ny_basic_bracket(self) -> None:
        self.assertAlmostEqual(income_tax_ny(8_000), 320.0)

    def test_progressive_monotonic(self) -> None:
        # Sanity: tax should not decrease when income increases
        self.assertGreater(income_tax_fed(50_000), income_tax_fed(10_000))
        self.assertGreater(income_tax_ca(50_000), income_tax_ca(10_000))
        self.assertGreater(income_tax_ny(50_000), income_tax_ny(10_000))


class TestCalculateIncomeTax(unittest.TestCase):
    def test_valid_inputs_ca(self) -> None:
        with patch("builtins.input", side_effect=["CA", "10000"]) as mock_input, \
             patch("sys.stdout", new=io.StringIO()) as fake_output:
            calculate_income_tax()

        output = fake_output.getvalue()
        self.assertIn("Your income is 10000 before tax", output)
        self.assertIn("after tax", output)
        self.assertIn("You pay", output)
        self.assertEqual(mock_input.call_count, 2)

    def test_invalid_state_then_valid(self) -> None:
        with patch("builtins.input", side_effect=["XX", "ma", "10000"]) as mock_input, \
             patch("sys.stdout", new=io.StringIO()) as fake_output:
            calculate_income_tax()

        output = fake_output.getvalue()
        self.assertIn("Invalid state", output)
        self.assertIn("Your income is 10000 before tax", output)
        self.assertEqual(mock_input.call_count, 3)

    def test_invalid_income_then_valid(self) -> None:
        with patch("builtins.input", side_effect=["NY", "abc", "-5", "5000"]) as mock_input, \
             patch("sys.stdout", new=io.StringIO()) as fake_output:
            calculate_income_tax()

        output = fake_output.getvalue()
        self.assertIn("Invalid income", output)
        self.assertIn("Income must be a non-negative integer.", output)
        self.assertIn("Your income is 5000 before tax", output)
        self.assertEqual(mock_input.call_count, 4)


if __name__ == "__main__":
    unittest.main()
