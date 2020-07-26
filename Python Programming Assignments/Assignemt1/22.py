#!/usr/bin/env python3
"""
Created on Wed Mar 25 10:17:27 2020

@author: Ashish Patel
"""
"""
 Write a Python program to convert a list of multiple integers into a single integer.
 
 Sample list: [11, 33, 50]
 Expected Output: 113350
 
 LOGIC:1)we take a list as a input.
       2)Then concatenate every element of it into a string.
       3)finally print that string.

"""
list = list(input("Enter  list: ").split(","))
s=str("")
for i in list:
    s = s + str(i)

print("final number by concatinating numbers of the list: " +s)