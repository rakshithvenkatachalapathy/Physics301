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
    import re

    parser = argparse.ArgumentParser()
    parser.add_argument('-x')
    # [-+]?[0-9]*\.+[0-9]*
    args = parser.parse_args()

    x = args.x
    m = re.match("[-+]?[0-9]*\.+[0-9]*", x)
    if re.match("[-+]?[0-9]*\.+[0-9]*", x):
        x = float(x)

    else:
        x = int(x)
    print(type(x))
    result = 0
    # based on the type of x call two functions
    if isinstance(x, int):
        result = fact(x - 1)
    else:
        print("hi")

    print(result)
