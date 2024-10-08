#!/usr/bin/python3
"""my attempt at pascals triangle
"""


from math import factorial


def pascal_triangle(n):
    # pascals traingle code

    triangle = []

    if type(n) is not int or n <= 0:
        return triangle

    for k in range(n):
        row = []
        for c in range(k + 1):
            ncr = factorial(k) // (factorial(c) * factorial(k - c))
            row.append(ncr)
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    print(pascal_triangle(n))
