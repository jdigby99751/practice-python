from JdPythonPractice.basic_recursion.factorial import factorial
import unittest


class TestCheckFactorial(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(factorial(5), 120)

    def test_case_2(self):
        self.assertEqual(factorial(6), 720)
