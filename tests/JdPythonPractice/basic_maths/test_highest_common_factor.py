from JdPythonPractice.basic_maths.highest_common_factor import hcf
import unittest


class TestCheckHighestCommonFactor(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(hcf(9, 12), 3)

    def test_case_2(self):
        self.assertEqual(hcf(12, 15), 3)

    def test_case_3(self):
        self.assertEqual(hcf(16, 24), 8)

    def test_case_4(self):
        self.assertEqual(hcf(17, 23), 1)

    def test_case_5(self):
        self.assertEqual(hcf(20, 15), 5)

    def test_case_6(self):
        self.assertEqual(hcf(20, 19), 1)
