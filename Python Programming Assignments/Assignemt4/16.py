#!/usr/bin/env python3
"""
Created on Thu Apr 16 10:23:36 2020

@author: Ashish Patel
"""
"""
Write a Pandas program to add, subtract, multiple, and divide two Pandas Series.
Example: Input Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
         Output: add: 3, 7, 11, 15, 19 
                 subtract: 1,1,1,1,1
                 multiply: 2, 12, 30, 56, 90 
                 divide: 2.000000, 1.333333, 1.200000, 1.142857, 1.111111

"""
import pandas
s1 = pandas.Series([2, 4, 6, 8, 10])
s2 = pandas.Series([1, 3, 5, 7, 9])

print("Add two Series:")
print(s1+s2)

print("Subtract two Series:")
print(s1-s2)

print("Multiply two Series:")
print(s1*s2)

print("Divide Series1 by Series2:")
print(s1/s2)