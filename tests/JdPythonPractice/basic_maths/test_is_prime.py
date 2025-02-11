from JdPythonPractice.basic_maths.is_prime import is_prime
import unittest


class TestCheckIsPrime(unittest.TestCase):
    def test_case_1(self):
        self.assertFalse(is_prime(1))

    def test_case_2(self):
        self.assertTrue(is_prime(2))

    def test_case_3(self):
        self.assertTrue(is_prime(3))

    def test_case_4(self):
        self.assertFalse(is_prime(4))

    def test_case_5(self):
        self.assertTrue(is_prime(5))

    def test_case_6(self):
        self.assertFalse(is_prime(6))

    def test_case_7(self):
        self.assertFalse(is_prime(16))

    def test_case_8(self):
        self.assertTrue(is_prime(19))

    def test_case_9(self):
        self.assertFalse(is_prime(1225))

    def test_case_10(self):
        self.assertTrue(is_prime(7919))

    def test_case_11(self):
        self.assertFalse(is_prime(7920))
