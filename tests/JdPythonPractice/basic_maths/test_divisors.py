from JdPythonPractice.basic_maths.divisors import divisors
import unittest


class TestCheckDivisors(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(divisors(1), [1])

    def test_case_2(self):
        self.assertEqual(divisors(2), [1, 2])

    def test_case_3(self):
        self.assertEqual(divisors(3), [1, 3])

    def test_case_4(self):
        self.assertEqual(divisors(4), [1, 2, 4])

    def test_case_5(self):
        self.assertEqual(divisors(36), [1, 2, 3, 4, 6, 9, 12, 18, 36])

    def test_case_6(self):
        self.assertEqual(divisors(100), [1, 2, 4, 5, 10, 20, 25, 50, 100])

    def test_case_7(self):
        self.assertEqual(divisors(12), [1, 2, 3, 4, 6, 12])
