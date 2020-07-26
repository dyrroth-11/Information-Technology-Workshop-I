#!/usr/bin/env python3
"""
Created on Tue Apr 7 09:58:17 2020

@author: Ashish Patel
"""
"""
Write python program to combine each line from first file with the corresponding line in second
file.

Input: Content of text file1 i.e., (Python Exercises, Java Exercises) and Content of
       text file_2 i.e., (Red, Green)

Output: Python Exercises
        Red
        Java Exercises
        Green

"""
with open('file_1.txt') as file1 , open('file_2.txt') as file2:
    for x in zip(*(file1 ,file2)):
        print(*x)