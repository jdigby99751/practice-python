from JdPythonPractice.basic_maths.is_armstrong_number import is_armstrong_number
import unittest


class TestCheckIsPalindrome(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(is_armstrong_number(153))

    def test_case_2(self):
        self.assertFalse(is_armstrong_number(152))

    def test_case_3(self):
        self.assertTrue(is_armstrong_number(371))
