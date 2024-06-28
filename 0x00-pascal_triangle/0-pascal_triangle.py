#!/usr/bin/python3
"""
This file contains the pascal_triangle function
"""


def pascal_triangle(n):
    """This function returns a list of lists of
    integers representing the Pascal’s triangle of n
    """
    result = []
    for i in range(n):
        currentRow = []
        for j in range(i+1):
            if j == 0 or j == i:
                currentRow.append(1)
            else:
                currentRow.append(result[i-1][j] + result[i-1][j-1])
        result.append(currentRow)
    return result
