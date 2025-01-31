from JdPythonPractice.array.rotate_array_by_k_elements import rotate_array
import unittest
from time import time


class TestCheckIfArrayIsSorted(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            rotate_array(7, [1, 2, 3, 4, 5, 6, 7], 2, "right"),
            [6, 7, 1, 2, 3, 4, 5]
        )

    def test_case_2(self):
        self.assertEqual(
            rotate_array(6, [3, 7, 8, 9, 10, 11], 3, "left"),
            [9, 10, 11, 3, 7, 8]
        )

    def test_case_3(self):
        self.assertEqual(
            rotate_array(7, [1, 2, 3, 4, 5, 6, 7], 2, "left"),
            [3, 4, 5, 6, 7, 1, 2]
        )
