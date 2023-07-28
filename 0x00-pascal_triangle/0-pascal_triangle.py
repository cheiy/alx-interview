#!/usr/bin/env python3


def pascal_triangle(n):
    """
    Function returns a list of lists of integers representing the
    Pascal's triangel of n
    """
    integers_list = []
    if n <= 0:
        return integers_list

    if n == 1:
        new_list = [1]
        integers_list.append(new_list)
        return integers_list

    if n == 2:
        integers_list = [[1]]
        new_list = [1, 1]
        integers_list.append(new_list)
        return integers_list

    triangle = [[1], [1, 1]]

    for i in range(2, n):
        temp = [1, 1]
        for j in range(0, len(triangle[-1])-1):
            a = triangle[-1][j]
            b = triangle[-1][j+1]
            temp.insert(-1, a + b)
        triangle.append(temp)

    return triangle
