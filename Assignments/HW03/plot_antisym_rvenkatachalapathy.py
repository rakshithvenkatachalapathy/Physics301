import argparse
import sys

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm, pyplot  # color map

from matplotlib import rc

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
rc('text', usetex=False)
rc('font', family='serif')

txt = "\n\nThe \"effective\" interaction between two neutral Fermions (both spin up) that arises from the symmetry " \
      "requirement on the total wave function. "


def f2(x, y):
    return np.sin(np.sqrt(np.power(x, 2) + np.power(y, 2)))


def antisym(x1, x2, n1=1, n2=2, a=1.0):
    pone = np.sin((n1 * np.pi * x1) / a) * np.sin((n2 * np.pi * x2) / a)
    ptwo = np.sin((n1 * np.pi * x2) / a) * np.sin((n2 * np.pi * x1) / a)
    val = (2 / a) * (pone - ptwo)
    return val


def parse_agrs():
    """
    This function is used to parse the user input using by using the argparse
    :return:
    """
    ret = ()
    parser = argparse.ArgumentParser()
    parser.add_argument('-x1_steps')
    parser.add_argument('-x2_steps')
    parser.add_argument('-n1')
    parser.add_argument('-n2')
    parser.add_argument('-a')
    args = parser.parse_args()
    # Read the command line input using argparse

    if len(sys.argv) == 5:
        x1 = int(args.x1_steps)
        x2 = int(args.x2_steps)
        n1 = 1
        n2 = 2
        a = 1.0
        ret = (x1, x2, n1, n2, a)
    elif len(sys.argv) == 11:
        x1 = int(args.x1_steps)
        x2 = int(args.x2_steps)
        n1 = int(args.n1)
        n2 = int(args.n2)
        a = float(args.a)
        ret = (x1, x2, n1, n2, a)
    return ret


if __name__ == "__main__":
    arg = parse_agrs()
    Z = 0

    fig = plt.figure(figsize=(9, 4))

    ax1 = fig.add_subplot(121, projection='3d')
    ax1.set_title('$Antisymmetric  Spatial  Wave  Function $')

    # x = y = np.linspace(-5, 5, 50)
    x = np.linspace(0, arg[4], arg[0])

    y = np.linspace(0, arg[4], arg[1])
    X, Y = np.meshgrid(x, y)
    Z = antisym(X, Y)
    Z2 = antisym(X, Y) ** 2

    ax1.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0)

    ax2 = fig.add_subplot(122, projection='3d')
    ax2.set_title('$  Probability Density$')

    ax2.plot_surface(X, Y, Z2, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0)
    fig.text(.5, .001, txt, ha='center')

    plt.ion()
    plt.show()

