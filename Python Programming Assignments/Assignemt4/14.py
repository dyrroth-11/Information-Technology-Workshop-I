#!/usr/bin/env python3
"""
Created on Thu Apr 16 09:58:02 2020

@author: Ashish Patel
"""
"""
Write a NumPy program to create a record array from a (flat) list of arrays.

Example: Arrays: [[1,2,3,4], ['Red', 'Green', 'White', 'Orange'], [12.20, 15.0, 20.0, 40.0]]
         Expected Output:
                        (1, 'Red', 12.2)
                        (2, 'Green', 15.0)
                        (3, 'White', 20.0)
                        (4, 'Orange', 40.0)

"""

import numpy 

x = numpy.array([1,2,3,4])
y = numpy.array(['Red','Green','White','Orange'])
z = numpy.array([12.20,15,20,40])
final = numpy.core.records.fromarrays([x,y,z],names='a,b,c,d')

for i in range(4):
	print(final[i])