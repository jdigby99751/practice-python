from JdPythonPractice.maths.polynomial import polynomial
import unittest
from scipy.integrate import quad
from math import factorial, e as math_e


class TestPolynomialIntegralValues(unittest.TestCase):
    """
    Test the polynomial class integral method by comparing the integral
    of the polynomial where the coefficient is the inverse factiorial of the
    coefficient order.

    """
    def test_polynomial_integral_values(self):
        """
        Test the polynomial class integral method by comparing the integral
        of the polynomial to the integral calculated by scipy quad function.

        The integral of the polynomial is calculated using the integral method
        of the polynomial class and the integral of the polynomial is
        calculated using the scipy quad function. The percent difference
        between the twointegrals is calculated and checked to be within 0.1%.

        The test is performed for polynomials of degree 0 to 10 with
        coefficients set to 1/i! for i in range 0 to i.
        """
        # Test over degree range from 0 to 10
        for i in range(0, 10):
            # set the coefficients to 1/i! for i in range 0 to i
            coefficients = [1 / (factorial(j)) for j in range(i + 1)]
            p = polynomial(coefficients)  # create polynomial
            # calculate the integral of the polynomial using scipy
            scipy_int = quad(p, 0, 1)[0]
            # calculate the integral of the polynomial using the
            # polynomial class
            p_int = p.integral(0, 1)
            print(f"p: {p}, scipy_int: {scipy_int}, p_int: {p_int}")
            # calculate the percent difference between the two integrals
            percent_diff = abs(scipy_int - p_int) / scipy_int * 100
            self.assertTrue(
                percent_diff < 0.1,
                f"scipy integral: {percent_diff}"
                f" is not within 0.1% of polynomial integral: {p_int}"
            )

    def test_polynomial_converge_to_e_minus_1(self):
        """
        For polynomials of degree 0 to 10 with coefficients set to 1/i!
        for i in range 0 to i. Test that the integral of the polynomial
        converges to e - 1 as the degree of the polynomial increases.
        The integral of the polynomial is calculated using the integral
        method of the polynomial class and the difference between the
        integral and e - 1 is calculated. The difference is checked to
        be less than the previous difference to check for convergence.
        """
        # set the convergence target to e - 1
        convergence_target = math_e - 1
        # initialize to a large number to check for convergence
        diff_to_target = 1000
        # Test over degree range from 0 to 10
        for i in range(0, 10):
            # set the coefficients to 1/i! for i in range 0 to i
            coefficients = [1 / (factorial(j)) for j in range(i + 1)]
            p = polynomial(coefficients)  # create polynomial
            p_int = p.integral(0, 1)  # calculate the integral
            diff = abs(p_int - convergence_target)
            self.assertTrue(
                diff < diff_to_target,
                f"Integral: {p_int} is not converging to {convergence_target}"
                f" for polynomial: {p}"
                f" with difference: {diff} and"
                f" previous difference: {diff_to_target}"
                f" for degree: {i}"
            )
            diff_to_target = diff
