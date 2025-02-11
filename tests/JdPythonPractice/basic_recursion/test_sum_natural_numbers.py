from JdPythonPractice.basic_recursion.sum_natural_numbers import sum_natural_numbers
import unittest


class TestCheckSumNaturalNumbers(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(sum_natural_numbers(10), 55)

    def test_case_2(self):
        self.assertEqual(sum_natural_numbers(6), 21)

