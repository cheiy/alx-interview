#!/usr/bin/python3
"""
Module contains a method/function that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Method determines if a given data set represents a valid UTF-8 encoding
    """
    count = 0
    for char in data:
        if count == 0:
            if char >> 5 == 6:
                count = 1
            elif char >> 4 == 14:
                count = 2
            elif char >> 3 == 30:
                count = 3
            elif char >> 7 != 0:
                return False
        else:
            if char >> 6 != 2:
                return False
            count -= 1
    return (count == 0)
