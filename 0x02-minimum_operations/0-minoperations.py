#!/usr/bin/python3
"""
Module contains the minOperations(n) function
"""


def minOperations(n):
    """
    Function calculates the minimum number of operations
    needed to produce exactly n H chars.
    """
    if not isinstance(n, int):
        return 0
    operations = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            operations += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            operations += 2
        elif clipboard > 0:
            done += clipboard
            operations += 1
    return operations
