from JdPythonPractice.array.remove_duplicates_from_sorted_array import remove_duplicates
import unittest
from time import time


class TestCheckIfArrayIsSorted(unittest.TestCase):
    def test_case_1(self):
        array = [1, 1, 2, 3, 3, 3, 4, 4, 5, 5]
        result = remove_duplicates(array)
        self.assertEqual(result, 5)
        self.assertEqual(array, [1, 2, 3, 4, 5])

    def test_case_2(self):
        array = [1, 1, 2, 3, 3, 4, 5, 5, 5]
        result = remove_duplicates(array)
        self.assertEqual(result, 5)
        self.assertEqual(array, [1, 2, 3, 4, 5])
