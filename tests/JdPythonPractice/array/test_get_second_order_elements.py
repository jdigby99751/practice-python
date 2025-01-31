from JdPythonPractice.array.get_second_order_elements import get_second_order_elements
import unittest
from time import time


class TestGetSecondOrderElements(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            get_second_order_elements(5, [1, 2, 3, 4, 5]),
            [4, 2]
        )

    def test_case_2(self):
        self.assertEqual(
            get_second_order_elements(5, [5, 4, 3, 2, 1]),
            [4, 2]
        )

    def test_case_3(self):
        self.assertEqual(
            get_second_order_elements(6, [1, 2, 3, 4, 5, 5]),
            [4, 2]
        )

    def test_case_4(self):
        self.assertEqual(
            get_second_order_elements(1, [1]),
            [None, None]
        )

    def test_case_5(self):
        self.assertEqual(
            get_second_order_elements(5, [4, 4, 3, 2, 1]),
            [3, 2]
        )

    def test_case_6(self):
        self.assertEqual(
            get_second_order_elements(5, [4, 1, 3, 2, 1]),
            [3, 2]
        )
