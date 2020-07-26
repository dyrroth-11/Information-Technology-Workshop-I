#!/usr/bin/env python3
"""
Created on Thu Apr 16 09:46:08 2020

@author: Ashish Patel
"""
"""
Write a NumPy program to find the number of elements of a given array, length of one array element in bytes,
and the total bytes consumed by the elements of the given array.

Example: Array = [1,2,3]
         Size of the array: 3
         Length of one array element in bytes: 8
         Total bytes consumed by the elements of the array: 24

"""
import numpy

A = numpy.array([1,2,3])

print("Size of the array: ", A.size)
print("Length of one array element in bytes: ", A.itemsize)
print("Total bytes consumed by the elements of the array: ", A.nbytes)