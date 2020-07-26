#!/usr/bin/env python3
"""
Created on Thu Apr 16 09:21:48 2020

@author: Ashish Patel
"""
"""
Write a NumPy program compute the sum of the diagonal elements of a given array.
Example: Original matrix: [[0 1 2]
                          [3 4 5]]
         Diagonal sum: 4

"""
import numpy
a = numpy.arange(6).reshape(2,3)
print("Original matrix:")
print(a)
dsum =  numpy.trace(a)
print("Condition number of the said matrix:")
print(dsum)