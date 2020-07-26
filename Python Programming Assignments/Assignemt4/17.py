#!/usr/bin/env python3
"""
Created on Thu Apr 16 10:37:28 2020

@author: Ashish Patel
"""
"""
Write a Python program to convert a NumPy array to a Pandas series.

Example: Sample Series:
NumPy array: [10 20 30 40 50]
Output: Converted Pandas series:
        0 10
        1 20
        2 30
        3 40
        4 50
        dtype: int64

"""

import numpy
import pandas
a = numpy.array([10, 20, 30, 40, 50])
print("NumPy array:")
print(a)
b = pandas.Series(a)
print("Converted Pandas series:")
print(b)