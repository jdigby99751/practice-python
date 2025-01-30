from JdPythonPractice.array.largest_element_in_array import largest_element
import unittest
from time import time


class TestLargestElementInArray(unittest.TestCase):
    def test_case_1(self):
        assert largest_element([1, 2, 3, 4, 5], 5) == 5

    def test_case_2(self):
        assert largest_element([5, 4, 3, 2, 1], 5) == 5

    def test_case_3(self):
        assert largest_element([1, 2, 3, 4, 5, 5], 6) == 5

    def test_case_4(self):
        assert largest_element([5, 4, 3, 2, 1, 5], 6) == 5

    def test_case_5(self):
        assert largest_element([1, 2, 3, 4, 5, 5, 5], 7) == 5

    def test_case_6(self):
        assert largest_element([5, 4, 3, 2, 1, 5, 5], 7) == 5

    def test_case_7(self):
        assert largest_element([1, 2, 3, 4, 5, 5, 5, 5], 8) == 5

    def test_case_8(self):
        assert largest_element([5, 4, 3, 2, 1, 5, 5, 5], 8) == 5

    def test_time_case_1(self):
        n = 10**6
        array = [1, 2, 3, 4, 5] * n
        print(f"Array length: {len(array)}")
        start_time = time()
        max_value = largest_element(array, n)
        print(f"Max value: {max_value}")
        end_time = time()
        run_time = end_time - start_time
        print(f"Run time: {run_time}")
        self.assertEqual(max_value, 5)
        self.assertLessEqual(run_time, 1)
