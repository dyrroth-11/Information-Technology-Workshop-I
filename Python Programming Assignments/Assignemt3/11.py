#!/usr/bin/env python3
"""
Created on Tue Apr 7 10:12:31 2020

@author: Ashish Patel
"""
"""
Write python program to read a random line from a file.

Input: Content of file test.txt

Output: languages such as C++ or Java.

"""
import random
x = open('test.txt').read().splitlines()
print(random.choice(x))