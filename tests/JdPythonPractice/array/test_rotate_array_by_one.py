from JdPythonPractice.array.rotate_array_by_one import rotate_array
import unittest
from time import time


class TestCheckIfArrayIsSorted(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            rotate_array([1, 2, 3, 4, 5], 5),
            [2, 3, 4, 5, 1]
        )

    def test_case_2(self):
        self.assertEqual(
            rotate_array([5, 4, 3, 2, 1], 5),
            [4, 3, 2, 1, 5]
        )

    def test_case_3(self):
        self.assertEqual(
            rotate_array([1, 2, 3, 4, 5, 5], 6),
            [2, 3, 4, 5, 5, 1]
        )

    def test_case_4(self):
        self.assertEqual(
            rotate_array([5, 4, 3, 2, 1, 5], 6),
            [4, 3, 2, 1, 5, 5]
        )

    def test_case_5(self):
        self.assertEqual(
            rotate_array([1, 2, 3, 4, 5, 5, 5], 7),
            [2, 3, 4, 5, 5, 5, 1]
        )

    def test_case_6(self):
        self.assertEqual(
            rotate_array([5, 4, 3, 2, 1, 5, 5], 7),
            [4, 3, 2, 1, 5, 5, 5]
        )

