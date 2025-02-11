from JdPythonPractice.basic_recursion.fibonacci import fibonacci_numbers, fibonacci
import unittest


class TestFibonacci(unittest.TestCase):
    def test_case_1(self):
        result = fibonacci(5)
        self.assertEqual(result, 5)

    def test_case_2(self):
        result = fibonacci(6)
        self.assertEqual(result, 8)


class TestFibonacciNumbers(unittest.TestCase):
    def test_case_1(self):
        result = fibonacci_numbers(5)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5])

    def test_case_2(self):
        result = fibonacci_numbers(6)
        self.assertEqual(result, [0, 1, 1, 2, 3, 5, 8])
