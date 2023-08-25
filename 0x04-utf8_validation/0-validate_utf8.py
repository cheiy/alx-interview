#!/usr/bin/python3
"""
Module contains a method/function that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Method determines if a given data set represents a valid UTF-8 encoding
    """
    flag = []
    for char in data:
        if char == 0 or char == 00 or char == 000:
            flag.append(1)
        elif char % 128 == 0 or char % 256 == 0:
            flag.append(0)
        else:
            flag.append(1)
    if flag.__contains__(0):
        return False
    else:
        return True
