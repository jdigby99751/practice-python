from JdPythonPractice.basic_recursion.is_palindrome_recursive import (
    is_palindrome_recursive as is_palindrome
)
import unittest


class TestCheckIsPalindrome(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(is_palindrome("1221"))

    def test_case_2(self):
        self.assertFalse(is_palindrome("race a car"))

    def test_case_3(self):
        self.assertTrue(is_palindrome("1"))

    def test_case_4(self):
        self.assertTrue(is_palindrome(" "))

    def test_case_5(self):
        self.assertTrue(is_palindrome("ABCDCBA"))

    def test_case_6(self):
        self.assertFalse(is_palindrome("TAKE U FORWARD"))

    def test_case_7(self):
        self.assertTrue(is_palindrome("123454321"))

    def test_case_8(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
