#!/usr/bin/env python3
"""
Created on Tue Apr 7 08:47:28 2020

@author: Ashish Patel
"""
"""
Write python program to count the number of lines in a text file.

Input: Content of test.txt

Output: Number of lines in the file: 4

"""
cnt=0
with open('test.txt') as file:
    for cnt,line in enumerate(file):
        continue
print("Number of lines in this file : "+str(cnt+1))