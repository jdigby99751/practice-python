from JdPythonPractice.basic_maths.reverse_digits import reverse_digits
import unittest


class TestCheckReverseDigits(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(reverse_digits(1234), 4321)

    def test_case_2(self):
        self.assertEqual(reverse_digits(1234567890), 987654321)

    def test_case_3(self):
        self.assertEqual(reverse_digits(0), 0)

    def test_case_4(self):
        self.assertEqual(reverse_digits(2), 2)

    def test_case_5(self):
        self.assertEqual(
            reverse_digits(
                123456789012345678901234567890123456789012345678901234567890
            ),
            98765432109876543210987654321098765432109876543210987654321
        )
