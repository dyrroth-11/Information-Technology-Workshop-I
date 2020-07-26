#!/usr/bin/env python3
"""
Created on Thu Apr 2 09:07:24 2020

@author: Ashish Patel
"""
"""
Write a Python program to calculate the harmonic sum of n-1.
Note: The harmonic sum is the sum of reciprocals of the positive integers.

Example : 1 + 1/2 + 1/3 + 1/4 + 1/5 + ....

LOGIC: In this we just defined a function which take n and input and loop through
       1 to n-1 and add its inverse value to sum and finally return sum.

 """
def sum(n):
    s = 0.0
    for i in range(1, n ):
        s = s + 1 / i
    return s

n = int(input("Enter the value of n: \n"))
print("Sum is", round(sum(n),6))