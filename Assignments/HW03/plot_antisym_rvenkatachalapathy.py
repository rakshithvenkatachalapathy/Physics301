#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import argparse
import math
import sys

import numpy as np


def antisym(x1, x2, n1=1, n2=2, a=1.0):
    print("ays")
    pone = math.sin(n1 * math.pi * x1 / a) * math.sin(n2 * math.pi * x2 / a)
    ptwo = math.sin(n1 * math.pi * x2 / a) * math.sin(n2 * math.pi * x1 / a)
    val = (2 / a) * (pone - ptwo)
    return val


def parse_agrs():
    """
    This function is used to parse the user input using by using the argparse
    :return:
    """
    ret = ()
    parser = argparse.ArgumentParser()
    parser.add_argument('-x1')
    parser.add_argument('-x2')
    parser.add_argument('-n1')
    parser.add_argument('-n2')
    parser.add_argument('-a')
    args = parser.parse_args()
    # Read the command line input using argparse

    if len(sys.argv) == 5:
        x1 = int(args.x1)
        x2 = int(args.x2)
        ret = (x1, x2)
    elif len(sys.argv) == 11:
        x1 = int(args.x1)
        x2 = int(args.x2)
        n1 = int(args.n1)
        n2 = int(args.n2)
        a = float(args.a)
        ret = (x1, x2, n1, n2, a)
    return ret


if __name__ == "__main__":
    arg = parse_agrs()
    if len(arg) == 2:
        print("2")
    elif len(arg) == 5:
        print("many")

