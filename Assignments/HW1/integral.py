"""
This the module for home work 1.

This module provides one function, intg() which is used to evaluate the value of an integral between a the given limits

There are two doctests below to test the integral of sin x and e^-x

>>> intg(sinx, 0, math.pi, 1e-7, False)[0]
1.9999999842068952

>>> intg(expw, 1, 3, 1e-7, False)[0]
0.3180923917632692

>>> (intg(sinx, 0, math.pi, 1e-7, False)[0] - ((-1* cos(math.pi)) - (-1*cos(0)))) < 1e-7
True

>>> (intg(expw, 1, 3, 1e-7, False)[0] - ((-1*math.exp(-3))-(-1*math.exp(-1)))) > 1e-7
False

>>> (intg(expw, 1, 3, 1e-7, False)[0] - ((-1*math.exp(-3))-(-1*math.exp(-1)))) < 1e-7
True
"""
import math
from math import pi, sin, cos

'''
Three lambda functions are defined below to evaluate three integrands
'''
sinx = lambda x: sin(x)

expw = lambda x: math.exp(-1 * x)

expr = lambda x: (x ** 3) / (math.exp(x) - 1)


def main():
    print('\nrunning...\n')
    lst = intg(expr, 0, 100)
    fract_err = abs(lst[0] - (math.pi ** 4 / 15))
    print('The integral evaluated to within specified accuracy: {:1.8f}'.format(lst[0]))
    print('The upper limit of its fractional error is estimated to be: {:1.8f}'.format(lst[1]))
    print('The correct answer is: {:1.8f}'.format(math.pi ** 4 / 15))
    print('The actual fractional error is: {:1.8f}%'.format(fract_err))


def intg(f, xlo, xhi, tol=1e-7, print_progress=True):
    """
    This function is used to evaluate the value of an integral function passed to it, between the given limits.
    The function executes until the fractional difference computed, falls below a certain tolerance level and prints the
    intermediate in a certain format

    :param f: function for which the integral needs to be evaluated
    :param xlo: the lower integration limit
    :param xhi: the upper integration limit
    :param tol: the tolerance level
    :param print_progress: a boolean flag used to suppress the printing statements

    :return: A tuple with two elements, the result of the integral and the final fractional difference

    """
    oldsum = 0
    newsum = 0
    fract_diff = 1
    dx = 1

    while fract_diff > tol:

        N = int((xhi - xlo) / dx)
        '''
        Find the sum of the area of the rectangle under the curves
        '''
        for i in range(0, N):
            if i == 0 and f == expr:
                result = 0
            else:
                result = f(xlo + (i * dx)) * dx
            newsum = newsum + result

        if print_progress:
            '''
            If print_progress is true , the print it out
            '''
            print('number of steps:{:5.0f}'.format(N))
            print('dy = {:1.5f} , integral = {:1.8f}'.format(dx, newsum))
            if dx == 1:
                print('frac_diff = N/A\n')
            else:
                print('frac_diff = {:1.8f}%\n'.format(fract_diff * 100))

        fract_diff = abs((newsum - oldsum) / newsum)
        oldsum = newsum
        if fract_diff > tol:
            newsum = 0
        dx = dx / 2


    return newsum, fract_diff


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    main()
