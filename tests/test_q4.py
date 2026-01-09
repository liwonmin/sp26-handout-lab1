"""Tests for Lab 1 Question 4"""

import sys
sys.path.append(".")

import unittest
from src.q4 import most_common_letter


class TestMostCommonLetter(unittest.TestCase):
    def test_simple_case(self) -> None:
        self.assertEqual(most_common_letter("apple"), "p")

    def test_ignore_case(self) -> None:
        self.assertEqual(most_common_letter("AaBbCcAa"), "a")

    def test_ignore_non_letters(self) -> None:
        self.assertEqual(most_common_letter("a!a?b,b."), "a")

    def test_tie_alphabetical(self) -> None:
        # a and b both appear twice -> return alphabetically first
        self.assertEqual(most_common_letter("bBaA"), "a")

    def test_single_letter(self) -> None:
        self.assertEqual(most_common_letter("Z"), "z")

    def test_no_letters(self) -> None:
        self.assertIsNone(most_common_letter("1234!!!"))

    def test_empty_string(self) -> None:
        self.assertIsNone(most_common_letter(""))


if __name__ == "__main__":
    unittest.main()
