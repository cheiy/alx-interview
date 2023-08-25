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
        elif char < 128 and char > -1:
            flag.append(1)
        elif char < 2048:
            if char % 256 == 0:
                flag.append(0)
            else:
                flag.append(1)
        elif char < 65536:
            if char % 256 == 0:
                flag.append(0)
            else:
                flag.append(1)
        elif char < 2097152:
            if char % 256 == 0:
                flag.append(1)
            else:
                flag.append(0)
        else:
            flag.append(0)
    if flag.__contains__(0):
        return False
    else:
        return True
