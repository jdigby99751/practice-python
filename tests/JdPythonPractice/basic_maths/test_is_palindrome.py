from JdPythonPractice.basic_maths.is_palindrome import is_palindrome
import unittest


class TestCheckIsPalindrome(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(is_palindrome(1221))

    def test_case_2(self):
        self.assertFalse(is_palindrome(1234))

    def test_case_3(self):
        self.assertTrue(is_palindrome(1))

    def test_case_4(self):
        self.assertTrue(is_palindrome(0))

    def test_case_5(self):
        self.assertTrue(is_palindrome(12321))

    def test_case_6(self):
        self.assertFalse(is_palindrome(12345))

    def test_case_7(self):
        self.assertTrue(is_palindrome(123454321))
