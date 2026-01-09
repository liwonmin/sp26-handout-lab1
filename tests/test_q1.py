"""Tests for Lab 1 Question 1"""

import unittest
from unittest.mock import Mock, call, patch

from src.q1 import validate_password


class TestValidatePassword(unittest.TestCase):
    """Test suite for validate_password function"""

    @patch("builtins.print")
    def test_valid_password(self, mock_print: Mock) -> None:
        self.assertTrue(validate_password("Valid1!a"))  # 8+ chars
        mock_print.assert_not_called()

    @patch("builtins.print")
    def test_too_short(self, mock_print: Mock) -> None:
        self.assertFalse(validate_password("V1!a"))
        mock_print.assert_called_with("Password must be at least 8 characters long")

    @patch("builtins.print")
    def test_missing_uppercase(self, mock_print: Mock) -> None:
        self.assertFalse(validate_password("valid1!@#"))
        mock_print.assert_called_with("Password must contain at least one uppercase letter")

    @patch("builtins.print")
    def test_missing_lowercase(self, mock_print: Mock) -> None:
        self.assertFalse(validate_password("VALID1!@#"))
        mock_print.assert_called_with("Password must contain at least one lowercase letter")

    @patch("builtins.print")
    def test_missing_digit(self, mock_print: Mock) -> None:
        self.assertFalse(validate_password("Valid!@#"))
        mock_print.assert_called_with("Password must contain at least one digit")

    @patch("builtins.print")
    def test_missing_special_character(self, mock_print: Mock) -> None:
        self.assertFalse(validate_password("Valid1234"))
        mock_print.assert_called_with(
            "Password must contain at least one special character (!@#$%^&*)"
        )

    @patch("builtins.print")
    def test_multiple_issues(self, mock_print: Mock) -> None:
        self.assertFalse(validate_password("short"))
        expected_calls = [
            call("Password must be at least 8 characters long"),
            call("Password must contain at least one uppercase letter"),
            call("Password must contain at least one digit"),
            call("Password must contain at least one special character (!@#$%^&*)"),
        ]
        mock_print.assert_has_calls(expected_calls, any_order=True)


if __name__ == "__main__":
    unittest.main()
