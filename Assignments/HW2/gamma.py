"""
This the module for home work 2.
This module is used to compute the value of the Gamma function based on the value of the user input
>>> fact(5)
120

>>> fact(10)
3628800

>> gamma(expr,1e-4,0,1000)[0]
52.34274485

#call_func internally calls gamma function

>>> call_func([5.5,1e-4])[0]
52.342744854260964

>>> call_func([6.0001,1e-4])[0]
120.02042110069128

>>> call_func([6.0000001,1e-4])[0]-fact(5) < 1e-4
True

"""
import sys
import sys
import doctest
import argparse
import math
import re
import pdb

'''
Importing the intg function from HW1 by traversing one level up in the folder structure and accessing HW1 folder
'''
sys.path.insert(0, '../HW1')
from integral import intg


def fact(n):
    """
    This function is used to calculate the factorial of a given number
    If the number is either 0 or 1, then we return the number
    :param n: the number for which the factorial has to be calculated
    :return: The computed factorial of the given number
    """
    # If n is less than 0, then we exit
    if n < 0:
        return
    # If n is either 0 or 1 , then we return the number
    if n == 0 or n == 1:
        return n
    # else we compute the factorial using a recursive call and return the sum
    else:
        sum = n * fact(n - 1)

    return sum


def gamma(f, tol, xlo, xhi):
    """
    This function is used to calculate the gamma function that is the integral of the given function
    Makes use of the intg function from HW1 to to evaluate the integral of the expression
    :param f: The function for which the integral needs to be evaluated
    :param tol: Tolerance level given to be 1e-4
    :param xlo: The lower integration limit
    :param xhi:The upper integration limit
    :return: A tuple with two elements, the result of the integral and the final fractional difference
    """
    res = intg(f, xlo, xhi, tol, False)
    return res


def parse_agrs():
    """
    This function is used to parse the user input using by using the argparse
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-x')
    parser.add_argument('-tol')
    args = parser.parse_args()
    # Read the command line input using argparse

    t = args.x
    tol = float(args.tol)
    # Check if the entered t value matches a floating point value
    if re.match("[-+]?[0-9]*\.+[0-9]*", t):
        t = float(t)

    else:
        t = int(t)

    return t, tol


def call_func(t):
    """
    This function is used to call wither fact or gamma function based on the value of 't' user input
    :param t: The tuple containing the value of t and tol
    :return: The result of gamma or factorial function
    """
    # If t is an instance of integer, then call factorial function
    if isinstance(t[0], int) and t[0] >= 1:
        result = fact(t[0] - 1)
    # Else call the gamma function
    elif isinstance(t[0], float) and t[0] >= 1:
        expr = lambda x: (x ** (t[0] - 1)) * math.exp(-1 * x)
        # result = intg(expr, 0, 1000, 1e-4, False)
        result = gamma(expr, t[1], 0, 1000)
    # If t is not greater than 1, then return
    else:
        print("The value of 't' is less than 1")
        result = 0

    return result


def print_details(final_result):
    """
    This function is used to print the final computed result
    :param final_result:  The  final result factorial or gamma function
    :return: NA
    """
    if isinstance(final_result, int):
        print('The factorial of t-1 is {:1}'.format(final_result))
    else:
        print('The result of the integral is {:1.8f}'.format(final_result[0]))
        print('The fract_diff is {:1.8f}'.format(final_result[1]))


if __name__ == "__main__":

    t = parse_agrs()
    # based on the type of x call two functions

    temp_result = call_func(t)

    print_details(temp_result)

'''
when you do parser.add_argument()
you can set -tol to have a default value, so that user can ignore it, like:
parser.add_argument('-tol', type = float, default = 1e-4)
'''