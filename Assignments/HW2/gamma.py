import sys

sys.path.insert(0, '../HW1')
from integral import intg


def fact(n):
    if n < 0:
        return
    sum = 0
    if n == 0 or n == 1:
        return n
    else:
        sum = n * fact(n - 1)

    return sum


def gamma(f, tol, xlo, xhi):
    res = intg(f, xlo, xhi, tol, False)
    return res


def parse_agrs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x')
    args = parser.parse_args()

    t = args.x
    if re.match("[-+]?[0-9]*\.+[0-9]*", t):
        t = float(t)

    else:
        t = int(t)

    return t


def call_func(t):
    if isinstance(t, int) and t >= 1:
        result = fact(t - 1)
    elif isinstance(t, float) and t >= 1:
        expr = lambda x: (x ** (t - 1)) * math.exp(-1 * x)
        # result = intg(expr, 0, 1000, 1e-4, False)
        result = gamma(expr, 1e-4, 0, 1000)
    else:
        print("The value of 't' is less than 1")
        result = 0

    return result


def print_details(final_result):
    if isinstance(final_result, int):
        print('The factorial of t-1 is {:1}'.format(final_result))
    else:
        print('The result of the integral is {:1.8f}'.format(final_result[0]))
        print('The fract_diff is {:1.8f}'.format(final_result[1]))


if __name__ == "__main__":
    import doctest
    import argparse
    import math
    import re
    import pdb

    t = parse_agrs()
    # based on the type of x call two functions

    temp_result = call_func(t)

    print_details(temp_result)

    # if isinstance(final_result, int):
    #     print('The factorial of t-1 is {:1}'.format(final_result))
    # else:
    #     print('The result of the integral is {:1.8f}'.format(final_result[0]))
    #     print('The fract_diff is {:1.8f}'.format(final_result[1]))

