def fact(n):
    if n < 0:
        return
    sum = 0
    if n == 0 or n == 1:
        return n
    else:
        sum = n * fact(n - 1)

    return sum


if __name__ == "__main__":
    import doctest
    import argparse
    import math

    parser = argparse.ArgumentParser()
    parser.add_argument('-x')
    # [-+]?[0-9]*\.+[0-9]*
    args = parser.parse_args()

    x = args.x
    print(type(x))

    # based on the type of x call two functions
