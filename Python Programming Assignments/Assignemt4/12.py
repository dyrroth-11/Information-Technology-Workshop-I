#!/usr/bin/env python3
"""
Created on Thu Apr 16 09:34:15 2020

@author: Ashish Patel
"""
"""
Write a NumPy program to create a 2d array with “1” and “0” only, where 1 is on the border and “0” is inside the
2d array.

Example:
Original array:
               [[ 1. 1. 1. 1. 1.]
                [ 1. 1. 1. 1. 1.]
                [ 1. 1. 1. 1. 1.]
                [ 1. 1. 1. 1. 1.]
                [ 1. 1. 1. 1. 1.]]
1 on the border and 0 is inside the 2d array.
               [[ 1. 1. 1. 1. 1.]
                [ 1. 0. 0. 0. 1.]
                [ 1. 0. 0. 0. 1.]
                [ 1. 0. 0. 0. 1.]
                [ 1. 1. 1. 1. 1.]]

"""
import numpy

n= int(input("Enter the value of n: \n"))
arr = numpy.ones((n,n))
arr[1:-1,1:-1] = 0

print(arr)