from JdPythonPractice.array.check_if_array_is_sorted import is_sorted
import unittest
from time import time


class TestCheckIfArrayIsSorted(unittest.TestCase):
    def test_case_1(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5], 5))

    def test_case_2(self):
        self.assertFalse(is_sorted([5, 4, 3, 2, 1], 5))

    def test_case_3(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 5], 6))

    def test_case_4(self):
        self.assertFalse(is_sorted([5, 4, 3, 2, 1, 5], 6))

    def test_case_5(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5, 5, 5], 7))

    def test_case_6(self):
        self.assertFalse(is_sorted([5, 4, 3, 2, 1, 5, 5], 7))

    def test_time_case_1(self):
        n = 10**6
        array = [1, 2, 3, 4, 5] * n
        print(f"Array length: {len(array)}")
        start_time = time()
        result = is_sorted(array, n * 5)
        end_time = time()
        run_time = end_time - start_time
        print(f"Run time: {run_time}")
        self.assertFalse(result)
        self.assertLessEqual(run_time, 1)

    def test_time_case_2(self):
        n = 10**6
        array = [1, 1, 1, 1, 1] * n
        print(f"Array length: {len(array)}")
        start_time = time()
        result = is_sorted(array, n * 5)
        end_time = time()
        run_time = end_time - start_time
        print(f"Run time: {run_time}")
        self.assertTrue(result)
        self.assertLessEqual(run_time, 1)
