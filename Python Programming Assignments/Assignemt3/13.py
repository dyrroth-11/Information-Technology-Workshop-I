#!/usr/bin/env python3
"""
Created on Tue Apr 7 10:45:08 2020

@author: Ashish Patel
"""
"""
Write python code to split the word from the input file.

Input: Python Exercises
       Java Exercises
Output: ['Python', 'Exercises']
        ['Java', 'Exercises']

"""
file = open('test.txt', 'r')
list = []
for line in file:
    for word in line.split():
        list.append(word)
print(list)