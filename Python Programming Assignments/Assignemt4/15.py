#!/usr/bin/env python3
"""
Created on Thu Apr 16 10:08:17 2020

@author: Ashish Patel
"""
"""
Write a NumPy program to take values from a source array and put them at specified indices of
another array.

Example: Input: [ 10. 10. 20. 30. 30.]
         Note: Put 0 and 40 in the first and fifth position of the above array.
         Output: [ 0. 10. 20. 30. 40.]

"""
import numpy

x = numpy.array([10, 10, 20, 30, 30])
print(x)
y = numpy.array([0, 40]) 
x.put([0,4], y)

print("Array x, after putting two values:")
print(A)