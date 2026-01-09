"""Tests for Lab 1 Question 2"""

import sys
import io
import unittest
from unittest.mock import patch

sys.path.append(".")
from src.q2 import set_password


class TestSetPassword(unittest.TestCase):
    """Test suite for set_password function"""

    def test_valid_password_on_first_try(self):
        """Should accept valid password immediately and exit"""
        simulated_inputs = ["GoodPass123!"]  # valid password

        with patch("builtins.input", side_effect=simulated_inputs), \
             patch("sys.stdout", new=io.StringIO()) as fake_output:

            set_password()

        output = fake_output.getvalue()
        self.assertIn("Password set successfully!", output)
        self.assertIn("GoodPass123!", output.lower())  # optional: check it was read

    def test_invalid_then_valid(self):
        """Should reject invalid password once, then accept valid one"""
        simulated_inputs = [
            "weak",                    # too short, no upper, no digit, no special
            "StrongPass123!"           # valid
        ]

        with patch("builtins.input", side_effect=simulated_inputs), \
             patch("sys.stdout", new=io.StringIO()) as fake_output:

            set_password()

        output = fake_output.getvalue()
        self.assertIn("Password set successfully!", output)
        # Check that error messages from validate_password appeared
        self.assertIn("at least 8 characters", output)
        self.assertIn("uppercase", output)
        self.assertIn("digit", output)
        self.assertIn("special", output)

    def test_multiple_invalid_attempts(self):
        """Should keep asking until valid password is provided"""
        simulated_inputs = [
            "abc",                     # very bad
            "password123",             # missing special + uppercase
            "PASSWORD!!!",             # missing lowercase + digit
            "MyGreatPassword2025!"     # valid
        ]

        with patch("builtins.input", side_effect=simulated_inputs), \
             patch("sys.stdout", new=io.StringIO()) as fake_output:

            set_password()

        output = fake_output.getvalue()
        self.assertIn("Password set successfully!", output)
        self.assertEqual(simulated_inputs.count("MyGreatPassword2025!"), 1)

        # Should have shown errors at least 3 times
        self.assertGreaterEqual(output.count("at least"), 3)
        self.assertGreaterEqual(output.count("Please try again"), 3)

    def test_empty_input_handling(self):
        """Should handle empty input gracefully (treat as invalid)"""
        simulated_inputs = [
            "",                        # empty
            "   ",                     # whitespace only
            "ValidPass123!"            # valid
        ]

        with patch("builtins.input", side_effect=simulated_inputs), \
             patch("sys.stdout", new=io.StringIO()) as fake_output:

            set_password()

        output = fake_output.getvalue()
        self.assertIn("Password set successfully!", output)
        self.assertIn("8 characters", output)  # length error should appear


if __name__ == "__main__":
    unittest.main()