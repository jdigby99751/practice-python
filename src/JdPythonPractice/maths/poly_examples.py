from JdPythonPractice.maths.polynomial import polynomial
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


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
