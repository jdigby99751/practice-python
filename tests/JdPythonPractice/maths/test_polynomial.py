from JdPythonPractice.maths.polynomial import polynomial
import unittest
import numpy as np
import numpy.testing as nptest
# from unittest.mock import patch, MagicMock


class TestPolynomial(unittest.TestCase):

    def test__init__case_1(self):
        with self.assertRaises(ValueError):
            polynomial(None)

        with self.assertRaises(ValueError):
            polynomial(1)

        with self.assertRaises(ValueError):
            polynomial([1, 2, 'a'])

    def test__init__case_2(self):
        p = polynomial([1, 2, 3])
        self.assertEqual(p.coefficients, [1, 2, 3])
        self.assertEqual(p.degree, 2)

    def test__init__case_3(self):
        p = polynomial([1, 2, 0])
        self.assertEqual(p.coefficients, [1, 2])
        self.assertEqual(p.degree, 1)

    def test__init__case_4(self):
        p = polynomial([0, 0, 0])
        self.assertEqual(p.coefficients, [0])
        self.assertEqual(p.degree, 0)

    def test__str__case_1(self):
        p = polynomial([1, 2, 3])
        self.assertEqual(str(p), "Polynomial of degree 2: 1 + 2x + 3x^2")

    def test__str__case_2(self):
        p = polynomial([1, 0, 2])
        self.assertEqual(str(p), "Polynomial of degree 2: 1 + 2x^2")

    def test__str__case_3(self):
        p = polynomial([0, 0, 0])
        self.assertEqual(str(p), "Polynomial of degree 0: 0")

    def test__str__case_4(self):
        p = polynomial([0, 0, 1])
        self.assertEqual(str(p), "Polynomial of degree 2: 1x^2")

    def test__str__case_5(self):
        p = polynomial([1, 0, 0, 0, 0, 3.1])
        self.assertEqual(str(p), "Polynomial of degree 5: 1 + 3.1x^5")

    def test__str__case_6(self):
        p = polynomial([1, 0, 0, 0, 0, 2])
        print(p)
        self.assertEqual(str(p), "Polynomial of degree 5: 1 + 2x^5")

    def test__call__case_1(self):
        p = polynomial([1, 2, 3])
        self.assertEqual(p(1), 6)

    def test__call__case_2(self):
        p = polynomial([1, 2, 3])
        self.assertEqual(p(2), 17)

    def test__call__case_3(self):
        p = polynomial([1, 2, 3])
        value = p(np.array([1, 2], np.int32))
        self.assertEqual(len(value), 2)
        nptest.assert_equal(value[0], 6)
        nptest.assert_equal(value[1], 17)

    def test__call__case_4(self):
        p = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p('a')

    def test__call__case_5(self):
        p = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p(None)

    def test_value_case_1(self):
        p = polynomial([1, 2, 3])
        self.assertEqual(p.value(1), 6)

    def test_value_case_2(self):
        p = polynomial([1, 2, 3])
        self.assertEqual(p.value(2), 17)

    def test_value_case_3(self):
        p = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p.value('a')

    def test_value_case_4(self):
        p = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p.value(None)

    def test_value_case_5(self):
        p = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p.value(np.array([1, 2], np.int32))

    # # Patch the show functionwith a mock to stop the plot displaying
    # @patch('matplotlib.pyplot.show')
    # # @patch('JD_Python_Practice.maths.polynomial.plt.show')
    # def test_plot_case_1(
    #     self,
    #     mock_show: MagicMock
    # ):
    #     p = polynomial([1, 2, 3])
    #     p.plot([-10, 10])
    #     mock_show.assert_called_once()

    def test__add__case_1(self):
        p1 = polynomial([1, 2, 3])
        p2 = polynomial([1, 2, 3])
        p3 = p1 + p2
        self.assertEqual(p3.coefficients, [2, 4, 6])

    def test__add__case_2(self):
        p1 = polynomial([1, 2, 3])
        p2 = polynomial([1, 2, 3, 4])
        p3 = p1 + p2
        self.assertEqual(p3.coefficients, [2, 4, 6, 4])

    def test__add__case_3(self):
        p1 = polynomial([1, 2, 3, 4])
        p2 = polynomial([1, 2, 3])
        p3 = p1 + p2
        self.assertEqual(p3.coefficients, [2, 4, 6, 4])

    def test__add__case_4(self):
        p1 = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p1 + 1

    def test__add__case_5(self):
        p1 = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p1 + 'a'

    def test__add__case_6(self):
        p1 = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p1 + None

    def test__add__case_7(self):
        p1 = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p1 + [1, 2, 3]

    def test__sub__case_1(self):
        p1 = polynomial([1, 2, 3])
        p2 = polynomial([1, 2, 3])
        p3 = p1 - p2
        self.assertEqual(p3.coefficients, [0])

    def test__sub__case_2(self):
        p1 = polynomial([1, 2, 3])
        p2 = polynomial([1, 2, 3, 4])
        p3 = p1 - p2
        self.assertEqual(p3.coefficients, [0, 0, 0, -4])

    def test__sub__case_3(self):
        p1 = polynomial([1, 2, 3, 4])
        p2 = polynomial([1, 2, 3])
        p3 = p1 - p2
        self.assertEqual(p3.coefficients, [0, 0, 0, 4])

    def test__sub__case_4(self):
        p1 = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p1 - 1

    def test__sub__case_5(self):
        p1 = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p1 - 'a'

    def test__sub__case_6(self):
        p1 = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p1 - None

    def test__sub__case_7(self):
        p1 = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p1 - [1, 2, 3]

    def test__mul__case_1(self):
        p1 = polynomial([1, 2, 3])
        p2 = polynomial([1, 2, 3])
        p3 = p1 * p2
        self.assertEqual(p3.coefficients, [1, 4, 10, 12, 9])

    def test__mul__case_2(self):
        p1 = polynomial([1, 2, 3])
        p2 = polynomial([1, 2, 3, 4])
        p3 = p1 * p2
        self.assertEqual(p3.coefficients, [1, 4, 10, 16, 17, 12])

    def test__mul__case_3(self):
        p1 = polynomial([1, 2, 3, 4])
        p2 = polynomial([1, 2, 3])
        p3 = p1 * p2
        self.assertEqual(p3.coefficients, [1, 4, 10, 16, 17, 12])

    def test__mul__case_4(self):
        p1 = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p1 * 1

    def test__mul__case_5(self):
        p1 = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p1 * 'a'

    def test__mul__case_6(self):
        p1 = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p1 * None

    def test__mul__case_7(self):
        p1 = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p1 * [1, 2, 3]

    # def test__div__case_1(self):
    #     p1 = polynomial([1, 2, 3])
    #     p2 = polynomial([1, 2, 3])
    #     p3 = p1 / p2
    #     self.assertEqual(p3.coefficients, [1])

    # def test__div__case_2(self):
    #     p1 = polynomial([1, 2, 3])
    #     p2 = polynomial([1, 2, 3, 4])
    #     p3 = p1 / p2
    #     self.assertEqual(p3.coefficients, [1])

    # def test__div__case_3(self):
    #     p1 = polynomial([1, 2, 3, 4])
    #     p2 = polynomial([1, 2, 3])
    #     p3 = p1 / p2
    #     self.assertEqual(p3.coefficients, [1])

    # def test__div__case_4(self):
    #     p1 = polynomial([1, 2, 3])
    #     with self.assertRaises(ValueError):
    #         p1 / 1

    # def test__div__case_5(self):
    #     p1 = polynomial([1, 2, 3])
    #     with self.assertRaises(ValueError):
    #         p1 / 'a'

    # def test__div__case_6(self):
    #     p1 = polynomial([1, 2, 3])
    #     with self.assertRaises(ValueError):
    #         p1 / None

    # def test__div__case_7(self):
    #     p1 = polynomial([1, 2, 3])
    #     with self.assertRaises(ValueError):
    #         p1 / [1, 2, 3]

    def test_Eculid_case_1(self):
        p1 = polynomial([1, 2, 3])
        p2 = polynomial([1, 2, 3])
        (p3, r3) = p1.Eculid(p2)
        self.assertAlmostEqual(p3.coefficients, [1])
        self.assertAlmostEqual(r3.coefficients, [0])
        # Check that p1 is not modified
        self.assertEqual(p1.coefficients, [1, 2, 3])
        # Check that p2 is not modified
        self.assertEqual(p2.coefficients, [1, 2, 3])

    def test_Eculid_case_2(self):
        p1 = polynomial([1, 2, 3])
        p2 = polynomial([1, 2, 3, 4])
        (p3, r3) = p1.Eculid(p2)
        self.assertAlmostEqual(p3.coefficients, [0])
        self.assertEqual(r3.coefficients, [1, 2, 3])
        # Check that p1 is not modified
        self.assertEqual(p1.coefficients, [1, 2, 3])
        # Check that p2 is not modified
        self.assertEqual(p2.coefficients, [1, 2, 3, 4])

    def test_Eculid_case_3(self):
        p1 = polynomial([1, 2, 3, 4])
        p2 = polynomial([1, 2, 3])
        (p3, r3) = p1.Eculid(p2)
        self.assertEqual(len(p3.coefficients), 2)
        self.assertEqual(len(r3.coefficients), 2)
        self.assertAlmostEqual(p3.coefficients[0], 0.1111111111)
        self.assertAlmostEqual(p3.coefficients[1], 1.3333333333)
        self.assertAlmostEqual(r3.coefficients[0], 0.8888888888)
        self.assertAlmostEqual(r3.coefficients[1], 0.4444444444)
        # Check that p1 is not modified
        self.assertEqual(p1.coefficients, [1, 2, 3, 4])
        # Check that p2 is not modified
        self.assertEqual(p2.coefficients, [1, 2, 3])

    def test_Eculid_case_4(self):
        p1 = polynomial([2, 5, 3])
        p2 = polynomial([1, 2])
        (p3, r3) = p1.Eculid(p2)
        self.assertEqual(len(p3.coefficients), 2)
        self.assertEqual(len(r3.coefficients), 1)
        self.assertAlmostEqual(p3.coefficients[0], 1.75)
        self.assertAlmostEqual(p3.coefficients[1], 1.5)
        self.assertAlmostEqual(r3.coefficients[0], 0.25)
        # Check that p1 is not modified
        self.assertEqual(p1.coefficients, [2, 5, 3])
        # Check that p2 is not modified
        self.assertEqual(p2.coefficients, [1, 2])

    def test_Eculid_case_5(self):
        p1 = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p1.Eculid(1)

    def test_Eculid_case_6(self):
        p1 = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p1.Eculid('a')

    def test_Eculid_case_7(self):
        p1 = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p1.Eculid(None)

    def test_Eculid_case_8(self):
        p1 = polynomial([1, 2, 3])
        with self.assertRaises(ValueError):
            p1.Eculid([1, 2, 3])

    def test_derivative_case_1(self):
        p = polynomial([1, 2, 3])
        p_prime = p.derivative()
        self.assertEqual(p_prime.coefficients, [2, 6])

    def test_derivative_case_2(self):
        p = polynomial([1, 2, 3, 4])
        p_prime = p.derivative()
        self.assertEqual(p_prime.coefficients, [2, 6, 12])

    def test_derivative_case_3(self):
        p = polynomial([1, 2])
        p_prime = p.derivative()
        self.assertEqual(p_prime.coefficients, [2])

    def test_derivative_case_4(self):
        p = polynomial([1])
        p_prime = p.derivative()
        self.assertEqual(p_prime.coefficients, [0])

    def test_derivative_case_5(self):
        p = polynomial([0])
        p_prime = p.derivative()
        self.assertEqual(p_prime.coefficients, [0])

    def test_derivative_case_6(self):
        p = polynomial([-1, -2, -3])
        p_prime = p.derivative()
        self.assertEqual(p_prime.coefficients, [-2, -6])

    def test_integral_case_1(self):
        p = polynomial([1, 2, 3])
        p_prime = p.integral()
        self.assertEqual(p_prime.coefficients, [0, 1, 1, 1])

    def test_integral_case_2(self):
        p = polynomial([1, 2, 3, 4])
        p_prime = p.integral()
        self.assertEqual(p_prime.coefficients, [0, 1, 1, 1, 1])

    def test_integral_case_3(self):
        p = polynomial([4, 3, 2, 1])
        p_prime = p.integral()
        self.assertEqual(
            p_prime.coefficients,
            [0, 4, 1.5, 0.6666666666666666, 0.25]
        )

    def test_integral_case_4(self):
        p = polynomial([1])
        p_prime = p.integral()
        self.assertEqual(p_prime.coefficients, [0, 1])

    def test_integral_case_5(self):
        p = polynomial([0])
        p_prime = p.integral()
        self.assertEqual(p_prime.coefficients, [0])

    def test_integral_case_6(self):
        p = polynomial([1, 2])
        p_prime = p.integral(1, 2)
        self.assertAlmostEqual(p_prime, 4)

    def test_integral_case_7(self):
        p = polynomial([3, 2, 1])
        p_prime = p.integral(1, 2)
        self.assertAlmostEqual(p_prime, 8.33333333333)

    def test_integral_case_8(self):
        p = polynomial([1, 2, 3, 4])
        p_prime = p.integral(1)
        self.assertEqual(p_prime.coefficients, [0, 1, 1, 1, 1])

    def test_integral_case_9(self):
        p = polynomial([1, 2, 3, 4])
        with self.assertRaises(ValueError):
            p.integral('a')

    def test_integral_case_10(self):
        p = polynomial([1, 2, 3, 4])
        with self.assertRaises(ValueError):
            p.integral(1, 'a')
