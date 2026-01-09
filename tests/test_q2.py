"""Tests for Lab 1 Question 2"""

import io
import unittest
from unittest.mock import Mock, patch

from src.q2 import set_password


class TestSetPassword(unittest.TestCase):
    """Test suite for set_password function"""

    def test_valid_password_on_first_try(self) -> None:
        """Should accept valid password immediately and exit"""
        simulated_inputs = ["GoodPass123!"]  # valid password

        with patch("builtins.input", side_effect=simulated_inputs) as mock_input, \
             patch("sys.stdout", new=io.StringIO()) as fake_output:
            set_password()

        output = fake_output.getvalue()
        self.assertIn("Please create a strong password.", output)
        self.assertIn("Password set successfully!", output)
        self.assertEqual(mock_input.call_count, 1)  # only asked once

    def test_invalid_then_valid(self) -> None:
        """Should reject invalid password once, then accept valid one"""
        simulated_inputs = [
            "weak",           # invalid
            "StrongPass123!"  # valid
        ]

        with patch("builtins.input", side_effect=simulated_inputs) as mock_input, \
             patch("sys.stdout", new=io.StringIO()) as fake_output:
            set_password()

        output = fake_output.getvalue()
        self.assertIn("Please try again with a stronger password.", output)
        self.assertIn("Password set successfully!", output)
        self.assertEqual(mock_input.call_count, 2)

        # Errors printed by validate_password for "weak"
        self.assertIn("Password must be at least 8 characters long", output)
        self.assertIn("Password must contain at least one uppercase letter", output)
        self.assertIn("Password must contain at least one digit", output)
        self.assertIn("Password must contain at least one special character", output)

    def test_multiple_invalid_attempts(self) -> None:
        """Should keep asking until valid password is provided"""
        simulated_inputs = [
            "abc",                 # invalid
            "password123",         # invalid (no uppercase, no special)
            "PASSWORD!!!",         # invalid (no lowercase, no digit)
            "MyGreatPassword2025!" # valid
        ]

        with patch("builtins.input", side_effect=simulated_inputs) as mock_input, \
             patch("sys.stdout", new=io.StringIO()) as fake_output:
            set_password()

        output = fake_output.getvalue()
        self.assertIn("Password set successfully!", output)
        self.assertEqual(mock_input.call_count, 4)

        # "Please try again..." should appear for each invalid attempt (3 times)
        self.assertGreaterEqual(output.count("Please try again with a stronger password."), 3)

    def test_empty_input_handling(self) -> None:
        """Should handle empty/whitespace input as invalid"""
        simulated_inputs = [
            "",             # empty
            "   ",          # whitespace only
            "ValidPass123!" # valid
        ]

        with patch("builtins.input", side_effect=simulated_inputs) as mock_input, \
             patch("sys.stdout", new=io.StringIO()) as fake_output:
            set_password()

        output = fake_output.getvalue()
        self.assertIn("Password set successfully!", output)
        self.assertEqual(mock_input.call_count, 3)

        # Empty string should trigger length requirement at least once
        self.assertIn("Password must be at least 8 characters long", output)


if __name__ == "__main__":
    unittest.main()
