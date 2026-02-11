#!/usr/bin/python3

"""12-pascal_triangle:
Representation of pascal's triangle with python
"""


def pascal_triangle(n):
    """Returns a list of integers that represent Pascal's triangle
    Args:
        n (int): number of rows in the triangle
    """
    if n <= 0:
        return []

    triangle = [[]] * n

    for i in range(n):
        triangle[i] = [1] * (i + 1)

        for j in range(i + 1):
            if j > 0 and j < i:
                triangle[i][j] = triangle[i - 1][j] + triangle[i - 1][j - 1]

    return triangle
