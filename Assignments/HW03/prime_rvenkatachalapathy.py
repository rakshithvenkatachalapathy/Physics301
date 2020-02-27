#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
HW03
Rakshith Venkatachalapathy
"""
import argparse

import numpy as np


def isprime(num):
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, num // 2):
            # If num is divisible by any number between   2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def parse_agrs():
    """
    This function is used to parse the user input using by using the argparse
    :return:
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
    lst = []
    for ix in range(start, end):
        if isprime(ix):
            lst.append(ix)

    primelist = np.array(lst)
    print(primelist)


if __name__ == "__main__":
    arg = parse_agrs()
    primes(arg[0], arg[1])

