#!/usr/bin/env python3
"""
Created on Thu Apr 2 07:59:16 2020

@author: Ashish Patel
"""
"""
Write a Python program to convert a list of tuples into a dictionary.

Example: Input: ((2, "w"),(3, "r"))
         Output: {'w': 2, 'r': 3}

 LOGIC: In this we just added the elements of tuple as key value of in a 
        dictionary and finally printed it.

 """
tuple = ((2, "w"),(3, "r"))
print(dict((j, i) for i, j in tuple))
