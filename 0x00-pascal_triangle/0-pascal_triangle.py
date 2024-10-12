#!/usr/bin/python3

"""pascals triangle attempt
"""

from math import factorial


def pascal_triangle(n):
    """function of pascals triangle"""

    triangle = [[1]]

    if n <= 0:
        return []

    else:
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)

    return triangle
