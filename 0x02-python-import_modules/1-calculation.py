#!/usr/bin/python3

if __name__ == "__main__":
    """Print the modulus, multiplication, division and subtraction of 10 and 5."""
    from calculator_1 import mod, mul, div, sub

    a = 10
    b = 5

    print("{} % {} = {}".format(a, b, mod(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))

