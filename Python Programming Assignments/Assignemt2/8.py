#!/usr/bin/env python3
"""
Created on Thu Apr 2 08:18:22 2020

@author: Ashish Patel
"""
"""
Write a Python program to find maximum and the minimum value in a set.

Example: Input: ([5, 10, 3, 15, 2, 20])
         Output: Maximum value: 20
                 Minimum value: 2

LOGIC:In this we take a set of numbers as input and then use max and min 
      method to find maximumm and minimum element of the set . finally 
      printed maximum and minimum values. 

 """
input_set = set(map(int,input("Enter space seperated values for set: \n").split()))
print("Maximum values: {}".format(max(input_set)))
print("Minimum value: {}".format(min(input_set)))