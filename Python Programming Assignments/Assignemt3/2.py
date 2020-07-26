#!/usr/bin/env python3
"""
Created on Tue Apr 7 07:27:12 2020

@author: Ashish Patel
"""
"""
Write python program to read first “n” lines of a file.

Input: test.txt

Output: What is Python language?
        Python is a widely used high-level, general-purpose, interpreted, dynamic programming
        language. Its design philosophy emphasizes code readability, and its syntax allows programmers
        to express concepts in fewer lines of code than possible in
        languages such as C++ or Java.

Note: Here the value of “n” is consider as 3.

"""
n = int(input("Enter the value of n i.e number of lines to be printed : "))
with open('test.txt') as x:
    nlines = [next(x) for i in range(n)]
for i in nlines:
    print(i)