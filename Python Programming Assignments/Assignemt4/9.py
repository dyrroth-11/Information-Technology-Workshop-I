#!/usr/bin/env python3
"""
Created on Thu Apr 16 08:56:18 2020

@author: Ashish Patel
"""
"""
Write a NumPy program to sort a given array of shape 2, along the first axis, last axis and on
flattened array.

Example:
Original array:
               [[10 40]
               [30 20]]
Expected Output:
               Sort the array along the first axis:
               [[10 20]
               [30 40]]
               Sort the array along the last axis:
               [[10 40]
               [20 30]]
               Sort the flattened array:
               [10 20 30 40]

"""
import numpy 
import math

A = numpy.array([[10,40],[30,20]])

print("Sort the array along the first axis:")
print(numpy.sort(A, axis=0))

print("Sort the array along the last axis:")
print(numpy.sort(A, axis=1))

print("Sort the flattened array:")
print(numpy.sort(A ,axis=None))