#!/usr/bin/python3
"""
Module contains a method/function that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Method determines if a given data set represents a valid UTF-8 encoding
    """
    flag = 0
    for char in data:
        if char % 128 == 0:
            flag = 0
            break
        else:
            flag = 1
    if flag == 0:
        return False
    else:
        return True
