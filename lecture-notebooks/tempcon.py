"""
>>> convert(0)
32.0

>>> convert(100)
212.0
"""
def convert(x):
    if x < -273.15:
        raise Exception("temp is below -273.125 !!")
    C = x * (9.0 / 5) + 32
    return C


if __name__ == "__main__":
    import doctest
    import argparse
    import math

    parser = argparse.ArgumentParser()
    parser.add_argument('-x', type=float)
    args = parser.parse_args()

    x = args.x

    y = convert(x)
    print(y)

