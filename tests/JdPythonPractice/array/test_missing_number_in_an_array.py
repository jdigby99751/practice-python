from JdPythonPractice.array.missing_number_in_an_array import missing_number, missing_number_xor
import unittest
from time import time


class TestMissingNumberInArray(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(missing_number([1, 2, 4, 5]), 3)

    def test_case_2(self):
        self.assertEqual(missing_number([1, 2, 3, 4, 5]), 6)

    def test_case_3(self):
        self.assertEqual(missing_number([2, 3, 4, 5]), 1)

    def test_case_4(self):
        self.assertEqual(missing_number_xor([1, 2, 4, 5]), 3)

    def test_case_5(self):
        self.assertEqual(missing_number_xor([1, 2, 3, 4, 5]), 6)

    def test_case_6(self):
        self.assertEqual(missing_number_xor([2, 3, 4, 5]), 1)

    # def test_time_case_1(self):
    #     n = 100000000
    #     test_array = [i for i in range(1, n)]
    #     start_time = time()
    #     result = missing_number(test_array)
    #     time_taken = time() - start_time
    #     self.assertEqual(result, n)

    #     start_time_xor = time()
    #     result_xor = missing_number_xor(test_array)
    #     time_taken_xor = time() - start_time_xor
    #     self.assertEqual(result_xor, n)

    #     print(f"Time taken by missing_number: {time_taken} compared to missing_number_xor: {time_taken_xor}")
    #     self.assertLessEqual(time_taken_xor, time_taken)

    # def test_time_case_2(self):
    #     n = 100000000
    #     test_array = [i for i in range(1, n)]

    #     start_time_xor = time()
    #     result_xor = missing_number_xor(test_array)
    #     time_taken_xor = time() - start_time_xor
    #     self.assertEqual(result_xor, n)

    #     start_time = time()
    #     result = missing_number(test_array)
    #     time_taken = time() - start_time
    #     self.assertEqual(result, n)
    #     print(f"Time taken by missing_number: {time_taken} compared to missing_number_xor: {time_taken_xor}")
    #     self.assertLessEqual(time_taken_xor, time_taken)
