#!/usr/bin/python3

"""demo script of function that takes n and calculates
fewest operations to result in n
"""


def minOperations(n):
    """function that checks for the fewest operations to n"""

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
