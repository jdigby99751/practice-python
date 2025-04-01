''' #ENG1002 Term 2 coursework, write your solutions in this file EXCLUSIVELY '''
import numpy as np
import numpy.typing as npt
from typing import Union, List, Self, Tuple
# from __future__ import annotations  # for Python 3.7
import matplotlib.pyplot as plt
from math import factorial, e as math_e
from scipy.integrate import quad, odeint
# import itertools


class polynomial():
    """
    A class to represent a polynomial using arrays to represent
    the polynomial coefficients.
    :param coefficients: A list of integers or floats representing the
    polynomial coefficients.
    :type coefficients: list[int, float]
    :ivar coefficients: The list of integers or floats representing this
    polynomial coefficients.
    :ivar degree: An integer representing the degree of this polynomial.
    :raises ValueError: Coefficients must be a list.
    :raises ValueError: Coefficients must be integers or floats.
    """

    def __init__(
        self,
        coefficients: List[Union[int, float]]
    ) -> Self:
        """
        Returns a polynomial using arrays to represent
        the polynomial coefficients.
        :param coefficients: A list of integers or floats representing the
        polynomial coefficients.
        :type coefficients: list[int, float]
        :ivar coefficients: The list of integers or floats representing this
        polynomial coefficients.
        :ivar degree: An integer representing the degree of this polynomial.
        :raises ValueError: Coefficients must be a list.
        :raises ValueError: Coefficients must be integers or floats.
        """
        # Check if the coefficients are a list
        if coefficients is None or isinstance(coefficients, list) is False:
            raise ValueError("Coefficients must be a list.")

        # Check if the coefficients are integers or floats
        i_last_non_zero = 0
        for i, v in enumerate(coefficients):
            if isinstance(v, (int, float)) is False:
                raise ValueError("Coefficients must be integers or floats.")
            if v != 0:
                i_last_non_zero = i
        if len(coefficients) == 0:
            self.coefficients = [0]  # cope with empty list
        else:
            # set attribute removing trailing zeros
            self.coefficients = coefficients[:i_last_non_zero + 1]
        # set the degree based on the length of the coefficients
        self.degree = len(self.coefficients) - 1

    def __str__(self) -> str:
        """
        Returns a string representation of this polynomial.
        :return: A string representation of this polynomial.
        :rtype: str
        """
        # Create a string representation of the polynomial
        s = f"Polynomial of degree {self.degree}: "
        if self.degree == 0:
            s += f"{self.coefficients[0]}"
            return s
        for i, v in enumerate(self.coefficients):
            if v == 0:
                continue  # skip zero coefficients

            s += f"{v}x^{i}" if i > 0 else f"{v}"

            # if i == 0:
            #     s += f"{v}"
            # else:
            #     s += f"{v}" if v != 1 else ""  # skip 1 coefficient
            #     s += "x"  # add x if degree > 0
            #     if i > 1:
            #         s += f"^{i}"  # add power if degree > 1
            if i < self.degree:
                s += " + "  # add plus sign if not last term
        print(s)
        return s

    def __call__(
        self,
        x: Union[int, float, npt.NDArray[np.float64]]
    ) -> Union[int, float, npt.NDArray[np.float64]]:
        """
        Evaluate the polynomial at a given value.
        :param x: The value at which to evaluate the polynomial.
        :type x: int, float, numpy.ndarray
        :return: The value of the polynomial at the given value.
        :rtype: int, float, numpy.ndarray
        :raises ValueError: Value must be an integer, float, or numpy array.
        """
        return_value = None
        if isinstance(x, (int, float)):
            # Evaluate the polynomial at the given value
            return_value = self.value(x)
        elif isinstance(x, np.ndarray):
            # Evaluate the polynomial for the each item in numpy array
            return_value = np.zeros(x.shape)
            for i, v in np.ndenumerate(x):  # iterate over the numpy array
                return_value[i] = self.value(v)
        else:
            raise ValueError(
                "Value must be an integer, float, or numpy array."
            )
        return return_value

    def value(
        self,
        x: Union[int, float]
    ) -> Union[int, float]:
        """
        Evaluate the polynomial at a given value.
        :param x: The value at which to evaluate the polynomial.
        :type x: int, float
        :return: The value of the polynomial at the given value.
        :rtype: int, float
        :raises ValueError: Value must be an integer or float.
        """
        return_value = None
        if isinstance(x, (int, float, np.integer, np.floating)):
            # Evaluate the polynomial at the given value
            return_value = 0
            for i, v in enumerate(self.coefficients):
                if i == 0:  # first term
                    return_value = v
                else:
                    if v != 0:  # skiping zero coefficients
                        return_value += v * x ** i
        else:
            raise ValueError(
                f"Value must be an integer or float not {type(x)}."
            )
        return return_value

    def plot(
        self,
        limits: List[Union[int, float]] = [0, 1]
    ) -> None:
        """
        Plots the polynomial between the given limits.
        :param limits: The limits of the plot.
        :type limits: list[int, float]
        :default limits: [0,1]
        :raises AssertionError: Limits must be a list of two values.
        :raises AssertionError: Limits must be in increasing order.
        :raises AssertionError: Limits must be integers or floats.
        """
        if limits is None:
            limits = [0, 1]  # default limits
        if len(limits) != 2:
            raise AssertionError("Limits must be a list of two values.")
        for i in limits:
            if not isinstance(i, (int, float)):
                raise AssertionError("Limits must be integers or floats.")
        if limits[0] >= limits[1]:
            raise AssertionError("Limits must be in increasing order.")

        x_array = np.linspace(
            start=limits[0],
            stop=limits[1],
            num=1001,
            endpoint=True)
        y_array = self.__call__(x_array)
        plt.plot(x_array, y_array)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend([str(self)])
        plt.title(f"Plot of the {self}")
        plt.show()

    def __add__(self, other) -> Self:
        """
        Adds two polynomials.
        :param other: The polynomial to add to this polynomial.
        :type other: polynomial
        :return: The sum of the two polynomials.
        :rtype: polynomial
        :raises ValueError: Other must be a polynomial.
        """
        if not isinstance(other, polynomial):
            raise ValueError("Other must be a polynomial.")

        degree_diff = self.degree - other.degree
        # find the longer polynomial and pad the shorter one with zeros
        if degree_diff > 0:
            self_coeffs = self.coefficients
            other_coeffs = other.coefficients + [0] * degree_diff
        else:
            self_coeffs = self.coefficients + [0] * abs(degree_diff)
            other_coeffs = other.coefficients

        new_coefficients = [sum(x) for x in zip(self_coeffs, other_coeffs)]
        # this would be a more efficient way to do the above
        # new_coefficients = [
        #     sum(x) for x in itertools.zip_longest(
        #         self.coefficients,
        #         other.coefficients,
        #         fillvalue=0)
        #     ]
        return polynomial(new_coefficients)

    def __sub__(self, other) -> Self:
        """
        Subtracts two polynomials.
        :param other: The polynomial to subtract from this polynomial.
        :type other: polynomial
        :return: The difference of the two polynomials.
        :rtype: polynomial
        :raises ValueError: Other must be a polynomial.
        """
        if not isinstance(other, polynomial):
            raise ValueError("Other must be a polynomial.")

        degree_diff = self.degree - other.degree
        # find the longer polynomial and pad the shorter one with zeros
        if degree_diff > 0:
            self_coeffs = self.coefficients
            other_coeffs = other.coefficients + [0] * degree_diff
        else:
            self_coeffs = self.coefficients + [0] * abs(degree_diff)
            other_coeffs = other.coefficients

        new_coefficients = [x - y for x, y in zip(self_coeffs, other_coeffs)]
        # this would be a more efficient way to do the above
        # new_coefficients = [
        #     x - y for x in itertools.zip_longest(
        #         self.coefficients,
        #         other.coefficients,
        #         fillvalue=0)
        #     ]
        return polynomial(new_coefficients)

    def __mul__(self, other) -> Self:
        """
        Multiplies two polynomials.
        :param other: The polynomial to multiply with this polynomial.
        :type other: polynomial
        :return: The product of the two polynomials."
        :rtype: polynomial"
        :raises ValueError: Other must be a polynomial."
        """
        if not isinstance(other, polynomial):
            raise ValueError("Other must be a polynomial.")

        new_degree = self.degree + other.degree
        new_coefficients = [0] * (new_degree + 1)
        for i, v1 in enumerate(self.coefficients):
            for j, v2 in enumerate(other.coefficients):
                new_coefficients[i + j] += v1 * v2
        return polynomial(new_coefficients)

    def Euclid(self, other) -> Tuple[Self, Self]:
        """
        Euclid division of two polynomials.
        :param other: The polynomial to divide this polynomial by.
        :type other: polynomial
        :return: The quotient and remainder of the two polynomials.
        :rtype: tuple(polynomial, polynomial
        :raises ValueError: Other must be a polynomial.
        :raises ValueError: Division by zero polynomial.
        :raises RuntimeError: Infinite loop protection.
        """
        if not isinstance(other, polynomial):
            raise ValueError("Other must be a polynomial.")

        if other.degree == 0 and other.coefficients[0] == 0:
            raise ValueError("Division by zero polynomial.")

        while_prot = 0  # protection from infinite loop

        qk = polynomial([0])  # quotient
        rl = self  # remainder
        d = other.degree  # degree of the other polynomial
        # leading coefficient of the other polynomial
        c = other.coefficients[-1]

        if rl.degree < d:
            # if the degree of the numerator is less than the degree of the
            # denominator, then the quotient is 0 and the remainder is the
            # numerator
            return (qk, rl)
        while rl.degree >= d:
            while_prot += 1
            if while_prot > 10000:
                raise RuntimeError("Infinite loop protection.")
            degree_diff = rl.degree - d
            # create polynomial with the leading coefficient of the
            # numerator/remainder divided by the leading coefficient of the
            # denominator
            st = polynomial([0] * degree_diff + [rl.coefficients[-1] / c])
            qk += st  # add the new polynomial to the quotient
            # subtract the new polynomial times the denominator
            rl -= st * other

        return (qk, rl)

    def derivative(self) -> Self:
        """
        Returns the derivative of the polynomial.
        :return: The derivative of the polynomial.
        :rtype: polynomial
        """
        new_coefficients = [i * v for i, v in enumerate(self.coefficients)][1:]
        return polynomial(new_coefficients)

    def integral(
        self,
        limit1: Union[int, float] = None,
        limit2: Union[int, float] = None
    ) -> Union[Self, float]:
        """
        Returns the integral of the polynomial.
        :param limit1: The lower limit of the integral.
        :type limit1: int, float
        :param limit2: The upper limit of the integral.
        :type limit2: int, float
        :return: The integral of the polynomial.
        :rtype: polynomial, float, int
        :raises ValueError: Limits must be integers or floats.
        """
        if limit1 is not None:
            if not isinstance(limit1, (int, float)):
                raise ValueError("Limits must be integers or floats.")
        if limit2 is not None:
            if not isinstance(limit2, (int, float)):
                raise ValueError("Limits must be integers or floats.")
        new_coefficients = [
            v / (i + 1) for i, v in enumerate(self.coefficients)
        ]  # coefficients for integral of the polynomial
        new_coefficients = [0] + new_coefficients  # set constant term to zero
        integral_poly = polynomial(new_coefficients)  # create polynomial
        if limit1 is not None and limit2 is not None:
            # calculate the integral between the limits
            return integral_poly(limit2) - integral_poly(limit1)
        else:
            return integral_poly


def testPolynomialIntegralValues():
    """
    Test the polynomial class integral method by comparing the integral
    of the polynomial to the integral calculated by scipy quad function.

    The integral of the polynomial is calculated using the integral method
    of the polynomial class and the integral of the polynomial is
    calculated using the scipy quad function. The percent difference
    between the twointegrals is calculated and checked to be within 0.1%.

    The test is performed for polynomials of degree 0 to 10 with
    coefficients set to 1/i! for i in range 0 to i.

    For polynomials of degree 0 to 10 with coefficients set to 1/i!
    for i in range 0 to i. Test that the integral of the polynomial
    converges to e - 1 as the degree of the polynomial increases.
    The integral of the polynomial is calculated using the integral
    method of the polynomial class and the difference between the
    integral and e - 1 is calculated. The difference is checked to
    be less than the previous difference to check for convergence.
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
        # print(f"p: {p}, scipy_int: {scipy_int}, p_int: {p_int}")
        # calculate the percent difference between the two integrals
        percent_diff = abs(scipy_int - p_int) / scipy_int * 100
        assert percent_diff < 0.1, f"scipy integral: {percent_diff}" + \
            f" is not within 0.1% of polynomial integral: {p_int}"

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
        assert diff < diff_to_target, f"Integral: {p_int} is not converging to {convergence_target}" + \
            f" for polynomial: {p}" + \
            f" with difference: {diff} and" + \
            f" previous difference: {diff_to_target}" + \
            f" for degree: {i}"

        diff_to_target = diff



def solveEquation():
    """
    Solve the equation y' + y + 3x + 2x^2 = 0
    using initial condition y(0) = -1
    """
    # Define the right hand side of the equation
    def f(y, x):
        return -y - 3*x - 2*x**2

    # Define the initial condition
    y0 = -1

    # Define the range of x values
    x = np.linspace(0, 1, 1001, endpoint=True)
    # Define the array to store the solution
    y = np.zeros(x.shape)
    y[0] = y0

    def euler_next_x(x, y):
        return y + 0.001 * f(y, x)
    # euler_next_x = lambda x, y: y + 0.001 * f(y, x)
    # solve the equation using Euler's method
    for i in range(1, 1001):
        y[i] = euler_next_x(x[i], y[i-1])
    # Solve the equation using odeint
    odeint_y = odeint(f, y0, x)

    return x, np.array(y), odeint_y


def verifySolution(p: polynomial) -> polynomial:
    """
    Verify the solution of the polynomial
    :param p: polynomial object
    :type p: polynomial
    :return: polynomial object
    :rtype: polynomial
    :raises TypeError: If the input is not a polynomial object
    """
    if not isinstance(p, polynomial):
        raise TypeError("Input must be a polynomial object")

    x, y, odeint_y = solveEquation()

    p_y = p(x)
    # p.plot([0, 1])
    # plt.plot(x_array, y_array)
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.title(f"Plot of the {self}")
    # plt.show()`
    plt.plot(x, p_y, label='Polynomial')
    plt.plot(x, y, label='Euler')
    plt.plot(x, odeint_y[:, 0], label='odeint')
    plt.legend()
    plt.show()

    r = p.derivative() + p + polynomial([0, 3, 2])

    # r.plot([0, 1])
    plt.plot(x, r(x), label='Residual')
    plt.plot(x, np.zeros(x.shape), label='0')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    return r


def solution():
    """
    Solve the equation y' + y + 3x + 2x^2 = 0
    """
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
        assert (coeff < 1e-5, f"coeff: {coeff} not close to 0")   


if __name__ == "__main__":
    # Test the polynomial class integral method
    testPolynomialIntegralValues()

    # # Define the polynomial
    # p = polynomial([1, 1, 3, 2])

    # # Verify the solution
    # verifySolution(p)
    # # print(p)
    # # print(p(1))
    # # print(p([1, 2, 3]))