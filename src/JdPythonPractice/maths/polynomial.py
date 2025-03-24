import numpy as np
import numpy.typing as npt
from typing import Union, List, Self, Tuple
# from __future__ import annotations  # for Python 3.7
import matplotlib.pyplot as plt
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
            s += f"{v}" if v != 1.0
            if i > 0:
            if i == 0:
                s += f"{v}"
            else:
                s += f"{v}" if v != 1 else ""  # skip 1 coefficient
                s += "x"  # add x if degree > 0
                if i > 1:
                    s += f"^{i}"  # add power if degree > 1
            if i < self.degree:
                s += " + "  # add plus sign if not last term
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
        limits: List[Union[int, float]] = None
    ) -> None:
        """
        Plots the polynomial between the given limits.
        :param limits: The limits of the plot.
        :type limits: list[int, float]
        :default limits: [0,1]
        :raises ValueError: Limits must be a list of two values.
        :raises ValueError: Limits must be in increasing order.
        :raises ValueError: Limits must be integers or floats.
        """
        if limits is None:
            limits = [0, 1]  # default limits
        if len(limits) != 2:
            raise ValueError("Limits must be a list of two values.")
        for i in limits:
            if not isinstance(i, (int, float)):
                raise ValueError("Limits must be integers or floats.")
        if limits[0] >= limits[1]:
            raise ValueError("Limits must be in increasing order.")

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

    def Eculid(self, other) -> Tuple[Self, Self]:
        """
        Eculid division of two polynomials.
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

    # def __truediv__(self, other) -> Self:
    #     """
    #     Divides two polynomials.
    #     :param other: The polynomial to divide this polynomial by.
    #     :type other: polynomial
    #     :return: The quotient of the two polynomials.
    #     :rtype: polynomial
    #     :raises ValueError: Other must be a polynomial.
    #     """
    #     if not isinstance(other, polynomial):
    #         raise ValueError("Other must be a polynomial.")

    #     return self.Eculid(other)[0]

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
