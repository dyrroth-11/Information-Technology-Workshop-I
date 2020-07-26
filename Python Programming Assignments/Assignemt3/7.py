#!/usr/bin/env python3
"""
Created on Tue Apr 7 09:13:51 2020

@author: Ashish Patel
"""
"""
Write python program to count the frequency of words in a file.

Input: Content of file test.txt

Output: Number of words in the file : Counter({'and': 6, 'a': 3, 'Python': 3, 'is': 3, ... })

"""
from collections import Counter
with open('test.txt') as file:
    print("Number of words in the file :" + str(Counter(file.read().split())))
