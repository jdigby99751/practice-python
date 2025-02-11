from JdPythonPractice.basic_maths.count_digits import count_digits
import unittest


class TestCheckCountDigits(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(count_digits(1234), 4)

    def test_case_2(self):
        self.assertEqual(count_digits(1234567890), 10)

    def test_case_3(self):
        self.assertEqual(count_digits(0), 1)

    def test_case_4(self):
        self.assertEqual(count_digits(2), 1)

    def test_case_5(self):
        self.assertEqual(
            count_digits(
                123456789012345678901234567890123456789012345678901234567890
            ),
        60)
