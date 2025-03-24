import unittest
# import numpy as np
import numpy.testing as nptest
from math import factorial
from JdPythonPractice.maths.poly_examples import (
    solveEquation,
    verifySolution
)
from JdPythonPractice.maths.polynomial import polynomial
# from unittest.mock import patch, MagicMock


class TestPolynomial(unittest.TestCase):

    def test_solveEquation(self):
        x, y, odeint_y = solveEquation()
        print(type(x))
        print(x)
        print(type(y))
        print(y)
        print(type(odeint_y))
        print(odeint_y[:, 0])
        nptest.assert_allclose(
            y, odeint_y[:, 0],
            rtol=1e-1,
        )

    def test_get_poly_for_solution(self):
        # Integrating factor = e^x
        # Taylor approximate e^x = 1 + x + x^2/2! + x^3/3! + ...
        p_e = polynomial([1 / (factorial(j)) for j in range(10)])
        # RHS = -3x - 2x^2 * Integrating factor
        p_i = polynomial([0, -3, -2]) * p_e
        # Integrate RHS
        p_n = p_i.integral()
        print(f" Exponential {p_e}")
        print(f" Numerator {p_n}")
        # Divide by integrating factor
        p_s, r_s = p_n.Eculid(p_e)
        print(f" quotient {p_s}")
        print(f" remainder {r_s}")
        print(f" p_s * p_e + r_s = {p_s * p_e + r_s}")

        assert True

    # @patch('matplotlib.pyplot.show')
    def test_verifySolution(
        self,
        # mock_show: MagicMock = None,
    ):
        # p = polynomial([-1/3, -4/3])
        # p = polynomial([-9.78181818, -1.418181818,
        #                 -0.409090909, -0.166666666])
        # Integrating factor = e^x
        # Taylor approximate e^x = 1 + x + x^2/2! + x^3/3! + ...
        def exp_poly_comp_minus(i: int) -> float:
            x = -1 if i % 2 != 0 else 1
            return x / (factorial(i))
        # Taylor approximate e^x = 1 + x + x^2/2! + x^3/3! + ...
        p_e = polynomial([1 / (factorial(j)) for j in range(10)])
        # Taylor approximate e^-x = 1 - x + x^2/2! - x^3/3! + ...
        p_e_minus_x = polynomial([exp_poly_comp_minus(j) for j in range(10)])
        # RHS = -3x - 2x^2 * Integrating factor
        p_i = polynomial([0, -3, -2]) * p_e
        # Integrate RHS
        p_n = p_i.integral()
        print(f"Exponential: {p_e}")
        print(f"Exponential Minus X: {p_e_minus_x}")
        print(f"Numerator: {p_n}")
        # Divide by integrating factor
        # p_s, r_s = p_n.Eculid(p_e)
        # print(f"Quotient: {p_s}")
        # print(f"Remainder: {r_s}")
        p_s = p_n * p_e_minus_x

        # constant of integration
        print(f"p_s(0): {p_s(0)}")
        c = -1 - p_s(0)
        print(f"c: {c}")
        # polynomial with constant of integration
        p_c = polynomial([c]) * p_e_minus_x

        p = p_s
        # p = p_s + r_s.Eculid(p_e)[0]
        # p = p_s + r_s
        # p = p_s + polynomial([r_s.coefficients[0]])
        # p = p_s + polynomial([c])
        # p = p_s + r_s.Eculid(p_e)[0] + r_s
        p = p_s + p_c
        print(f"p: {p}")

        r = verifySolution(p)
        print(f"r: {r}")
        for coeff in r.coefficients:
            self.assertTrue(coeff < 1e-5, f"coeff: {coeff} not close to 0")

        # assert False
