'''Unit testing module for the python part of the ENG1002 term 2 coursework
   Execute this file to test your solutions'''

import numpy as np
from ENG1002_Term_2_Coursework_2025 import polynomial, solveEquation, verifySolution

def testPolynomialConstructor():
    '''Function to test the constructor of the polynomial class '''
    
    print('Testing polynomial class constructor')
    
    poly1 = polynomial([1,2,3,4,5])
    poly2 = polynomial([0,2.5,3.0])
    poly3 = polynomial([])
    poly4 = polynomial([0.2,1.4,5.7,0,0.0,0])
    poly5 = polynomial([0,0,0,0])

    assert poly1.degree == 4, 'The polynomial class constructor does not assign the degree attribute correctly for a polynomial of degree 4'
    assert poly2.degree == 2, 'The polynomial class constructor does not assign the degree attribute correctly for a polynomial of degree 2'
    assert poly3.degree == 0, 'The polynomial class constructor does not assign the degree attribute correctly for an empty polynomial'
    assert poly4.degree == 2, 'The polynomial class constructor does not assign the degree attribute correctly for a polynomial with zero coefficients for the higher degree terms'
    assert poly5.degree == 0, 'The polynomial class constructor does not assign the degree attribute correctly for a polynomial with zero coefficients'
    
    assert poly1.coefficients == [1,2,3,4,5], 'The polynomial class constructor does not assign the coefficients atrtribute correctly'
    assert poly2.coefficients == [0,2.5,3.0], 'The polynomial class constructor does not assign the coefficients atrtribute correctly'
    assert poly3.coefficients == [0], 'The polynomial class constructor does not assign the coefficients atrtribute correctly for an empty list'
    assert poly4.coefficients == [0.2,1.4,5.7], 'The polynomial class constructor does not assign the coefficients atrtribute correctly for a list with zeros at the end'
    assert poly5.coefficients == [0], 'The polynomial class constructor does not assign the coefficients atrtribute correctly for a list with zeros'
    
    try:
        polynomial('wrong input')
    except:
        pass
    else:
        raise TypeError('The polynomial class constructor should raise an error when the provided input argument is not a list')
        
    try:
        polynomial([1,2,3,4,'wrong input'])
    except:
        pass
    else:
        raise TypeError('The polynomial class constructor should raise an error when the provided list does not contain numbers')
    
    print('Polynomial class constructor tests successful!')
    
def testPolynomialStr():
    '''Function to test the __str__ method of the polynomial class '''
    
    print('Testing __str__ method of polynomial class')
    
    poly1 = polynomial([1,2,3,4,5])
    poly2 = polynomial([])
    
    assert poly1.__str__() == 'Polynomial of degree 4: 1 + 2x^1 + 3x^2 + 4x^3 + 5x^4', 'The __str__ method does not print polynomials properly'
    assert poly2.__str__() == 'Polynomial of degree 0: 0', 'The __str__ method does not print zero polynomials properly'
    
    print('__str__ method tests successful!')
    
def testPolynomialCall():
    '''Function to test the __call__ method of the polynomial class '''
    
    print('Testing __call__ method of polynomial class')
    
    poly = polynomial([1,2,3,4,5])
    
    try:
        poly('wrong input')
    except:
        pass
    else:
        raise TypeError('The __call__ method should raise an error when the provided input is not an array or number')
    
    assert poly(1)==15, 'The __call_ method does not evaluate the polynomial correctly for numerical inputs'
    
    x = np.linspace(0,10,101);
    
    p = 1+2*x+3*x**2+4*x**3+5*x**4
    
    assert np.max(np.abs(poly(x)-p))<1e-6, 'The __call__ method does not evaluate the polynomial correctly for array inputs'
    
    print('__call__ method tests successful!')
    
def testPolynomialPlot():
    '''Function to test the plot method of the polynomial class '''
    
    print('Testing plot method of polynomial class')
    
    poly = polynomial([1,2,3,4,5])
    
    try:
        poly.plot('wrong input')
    except AssertionError:
        pass
    except:
        raise TypeError('The plot method should raise an assertion error when the provided input is not a list')
    else:
        raise TypeError('The plot method should raise an assertion error when the provided input is not a list')
        
    try:
        poly.plot([1])
    except AssertionError:
        pass
    except:
        raise TypeError('The plot method should raise an assertion error when the provided input is not a list of size 2')
    else:
        raise TypeError('The plot method should raise an assertion error when the provided input is not a list of size 2')
        
    try:
        poly.plot(['wrong input',2])
    except AssertionError:
        pass
    except:
        raise TypeError('The plot method should raise an assertion error when the provided input is not a list of size 2 containing numbers')
    else:
        raise TypeError('The plot method should raise an assertion error when the provided input is not a list of size 2 containing numbers')
    
    print('plot method tests successful!')
    
def testPolynomialAddSub():
    '''Function to test the __add__ and __sub__ methods of the polynomial class '''
    
    print('Testing __add__ method of polynomial class')
    
    p1 = polynomial([1,2,3])
    p2 = polynomial([4,3,2])
    p3 = polynomial([1,0,8,7])
    
    try:
        p1+p2
    except:
        raise Exception('Polynomial addition not defined properly')
    else:
        assert type(p1+p2)==polynomial, 'The result of polynomial addition should be a polynomial'
    
    try:
        p1+p3
    except:
        raise Exception('Polynomial addition sould be able to handle polynomials of different degrees')
        
    try:
        p3+p1
    except:
        raise Exception('Polynomial addition sould be able to handle polynomials of different degrees')
        
    try:
        p1-p2
    except:
        raise Exception('Polynomial subtraction not defined properly')
    else:
        assert type(p1-p2)==polynomial, 'The result of polynomial subtraction should be a polynomial'
    
    try:
        p1-p3
    except:
        raise Exception('Polynomial subtraction sould be able to handle polynomials of different degrees')
        
    try:
        p3-p1
    except:
        raise Exception('Polynomial subtraction sould be able to handle polynomials of different degrees')
    
    print('__add__ method tests successful!')
    
def testPolynomialMul():
    '''Function to test the __mul__ method of the polynomial class '''
    
    print('Testing __mul__ method of polynomial class')
    
    p1 = polynomial([1,2,3])
    p2 = polynomial([4,3,2,5])
    
    try:
        p1*p2
    except:
        raise Exception('Polynomial multiplication not defined properly')
    else:
        assert type(p1*p2)==polynomial, 'The result of polynomial multiplication should be a polynomial'
    
    print('__mul__ method tests successful!')
    
def testPolynomialEuclid():
    '''Function to test the Euclid method of the polynomial class '''
    
    print('Testing Euclid method of polynomial class')
    
    p1 = polynomial([2,6,1,8,4,12])
    p2 = polynomial([1,2,2])
    p3 = polynomial([0])
    
    try:
        q,r = p1.Euclid(p2)
    except:
        raise Exception('Euclid method not defined properly')
    else:
        assert type(q)==polynomial,'The quotient of the division of two polynomials should be a polynomial'
        assert type(r)==polynomial,'The remainder of the division of two polynomials should be a polynomial'
        
    try:
        q,r = p1.Euclid(p3)
    except:
        pass
    else:
        raise TypeError('The Euclid method should raise an error when the provided input argument is a zero polynomial')
        
    print('Euclid method tests successful!')
    
def testPolynomialDerivative():
    '''Function to test the derivative method of the polynomial class '''
    
    print('Testing derivative method of polynomial class')
    
    try:
        polynomial([1,2,3]).derivative()
    except:
        raise Exception('Derivative not defined properly')    
        
    print('derivative method tests successful!')
    
def testPolynomialIntegral():
    '''Function to test the integral method of the polynomial class '''
    
    print('Testing integral method of polynomial class')
    
    try:
        polynomial([1,2,3]).integral()
        polynomial([1,2,3]).integral(0,1)
    except:
        raise Exception('integral not defined properly')
        
    assert type(polynomial([2,5,4]).integral())==polynomial, 'The polynomial integral method should return a polynomial object when called without any input arguments'
    assert type(polynomial([2,5,4]).integral(0,1.5))==float, 'The polynomial integral method should return a number when called with numerical input arguments'
    
    print('integral method tests successful! Run your testPolynomialIntegralValues function to further test the method.')
    
def testPolynomialDoc():
    '''Function to test the documentation of the polynomial class '''
    
    print('Testing polynomial class documentation')
    
    assert polynomial.__doc__!=None, 'The polynomial class documentation is empty'
    assert polynomial.__init__.__doc__!=None, 'The polynomial class constructor documentation is empty'
    assert polynomial.__str__.__doc__!=None, 'The polynomial class __str__ method documentation is empty'
    assert polynomial.__call__.__doc__!=None, 'The polynomial class __call__ method documentation is empty'
    assert polynomial.plot.__doc__!=None, 'The polynomial class plot method documentation is empty'
    assert polynomial.__add__.__doc__!=None, 'The polynomial class __add__ method documentation is empty'
    assert polynomial.__sub__.__doc__!=None, 'The polynomial class __sub__ method documentation is empty'
    assert polynomial.__mul__.__doc__!=None, 'The polynomial class __mul__ method documentation is empty'
    assert polynomial.derivative.__doc__!=None, 'The polynomial class derivative method documentation is empty'
    assert polynomial.integral.__doc__!=None, 'The polynomial class integral method documentation is empty'
    
    print('Documentation tests successful')
    
def testSolveEquation():
    '''Function to test the solveEquation function '''
    
    print('Testing solveEquation function')
    
    assert type(solveEquation())==tuple and len(solveEquation())==2 , 'The solveEquation function should return two output arguments'
    
    x,y = solveEquation()
    
    assert type(x)==np.ndarray and type(y)==np.ndarray,'The outputs of solveEquation should be numpy arrays'
    
    assert x.size == 1001 and y.size == 1001, 'The size of the arrays returned by solveEquation should be 1001'
    
    assert solveEquation.__doc__!=None, 'The documentation of the solveEquation function is empty'
    
    print('solveEquation tests successful')
    
def testVerifySolution():
    '''Function to test the verifySolution function '''
    
    print('Testing verifySolution function')

    try:    
        verifySolution(3)
    except:
        pass
    else:
        raise Exception('The verifySolution function should raise an exception if the provided argument is not a polynomial')
    
    r = verifySolution(polynomial([-1,1,-2]))
    
    assert type(r) == polynomial, 'The output of verifySolution should be a polynomial'
    
    assert verifySolution.__doc__!=None, 'The documentation of the verifySolution function is empty'
    
    print('verifySolution tests successful')

if __name__=='__main__':
    testPolynomialConstructor()
    testPolynomialStr()
    testPolynomialCall()
    testPolynomialPlot()
    testPolynomialAddSub()
    testPolynomialMul()
    testPolynomialEuclid()
    testPolynomialDerivative()
    testPolynomialIntegral()
    testPolynomialDoc()
    
    testSolveEquation()
    testVerifySolution()