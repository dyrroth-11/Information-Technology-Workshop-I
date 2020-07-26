#!/usr/bin/env python3
"""
Created on Tue Apr 7 08:02:49 2020

@author: Ashish Patel
"""
"""
Write python program to read last “n” lines of a file.

Input: Content of test.txt

Output: languages such as C++ or Java. (till last line)

Note: Here the value of “n” is consider as 2.

"""
n=int(input("Enter the value of n i.e the number of last n lines you want to read :"))
with open('test.txt') as file:
    for line in (file.readlines()[-n:]):
        print(line)