from JdPythonPractice.array.move_zeros_to_end import move_zeros
import unittest
from time import time


class TestCheckIfArrayIsSorted(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            move_zeros(6, [0, 1, 2, 3, 4, 5]),
            [1, 2, 3, 4, 5, 0]
        )

    def test_case_2(self):
        self.assertEqual(
            move_zeros(5, [5, 0, 3, 0, 1]),
            [5, 3, 1, 0, 0]
        )

    def test_case_3(self):
        self.assertEqual(
            move_zeros(6, [0, 5, 4, 3, 2, 1]),
            [5, 4, 3, 2, 1, 0]
        )

    def test_case_4(self):
        self.assertEqual(
            move_zeros(5, [0, 0, 0, 0, 0]),
            [0, 0, 0, 0, 0]
        )

    def test_case_5(self):
        self.assertEqual(
            move_zeros(5, [1, 2, 3, 4, 5]),
            [1, 2, 3, 4, 5]
        )

    def test_case_6(self):
        self.assertEqual(
            move_zeros(5, [0, 0, 0, 0, 1]),
            [1, 0, 0, 0, 0]
        )

    def test_case_7(self):
        self.assertEqual(
            move_zeros(10, [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]),
            [1, 2, 3, 2, 4, 5, 1, 0, 0, 0]
        )