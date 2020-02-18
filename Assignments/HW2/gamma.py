if __name__ == "__main__":
    import doctest
    import argparse
    import math

    parser = argparse.ArgumentParser()
    parser.add_argument('-x', type=float)
    args = parser.parse_args()

    x = args.x