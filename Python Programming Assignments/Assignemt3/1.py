#!/usr/bin/env python3
"""
Created on Tue Apr 7 07:18:28 2020

@author: Ashish Patel
"""
"""
Write python program to read the entire test.txt file.

Input: test.txt

Output: Content of file test.txt. i.e., What is Python language?
        Python is a widely used high-level, general-purpose, interpreted, dynamic programming
        language. Its design philosophy emphasizes code readability, and its syntax allows programmers
        to express concepts in fewer lines of code than possible in
        languages such as C++ or Java. (till last line)

 """
a = open('test.txt')
print(a.read())