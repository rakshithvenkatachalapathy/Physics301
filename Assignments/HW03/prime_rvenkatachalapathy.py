"""
HW03
Rakshith Venkatachalapathy

This module is for HW03 to calculate the primes between two numbers
Please provide the first number with the -s identifier and the second number with the -e identifier

>>> primes(1,3)
[1 2 3]

>>> primes(1,5)
[1 2 3 5]

>>> primes(1,11)
[ 1  2  3  5  7 11]

>>> isprime(11) == 11
True
"""
import argparse

import numpy as np


def isprime(num):
    """
    Checks if a number is prime and returns a prime
    :param num: number
    :return: returns  a number if prime

    >>> isprime(11) == 11
    True
    """

    if num == 1:
        return num

    if num > 1:
        # Iterate from 2 to num
        for i in range(2, num):
            # If num is divisible by any number between   2 and n  it is not prime
            if (num % i) == 0:
                break
        else:
            return num


def parse_agrs():
    """
    This function is used to parse the user input using by using the argparse
    :return: A tuple with the start and end
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-s')
    parser.add_argument('-e')
    args = parser.parse_args()
    # Read the command line input using argparse
    s = int(args.s)
    e = int(args.e)
    return s, e


def primes(start, end):
    """
    This function calculates the prime numbers in a given range and prints it out
    :param start: range start
    :param end: range end
    :return: NA
    """
    lst = []
    for ix in range(start, end + 1):
        if isprime(ix):
            lst.append(ix)

    primelist = np.array(lst)
    print(primelist)


if __name__ == "__main__":
    arg = parse_agrs()
    primes(arg[0], arg[1])

'''
    try this one to save one for loop:
        def find_prime(minint, maxint):
        import numpy as np
        ints = np.arange(1, maxint+1)
        primenum = []
        for i in range(minint, maxint+1):
            rmdr = i%ints
            if np.sum(rmdr == 0) == 2:
                primenum.append(i)
        return primenum
    '''