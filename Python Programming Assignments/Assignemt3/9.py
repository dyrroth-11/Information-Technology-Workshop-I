#!/usr/bin/env python3
"""
Created on Tue Apr 7 09:45:13 2020

@author: Ashish Patel
"""
"""
Write python program to write a list content to a file.

Input: color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

Output: Red
        Green
        White
        Black
        Pink
        Yellow

"""
list = list(input("Enter a list : \n").split())
with open('q9.txt', "w") as file:
    for x in list:
        file.write(x + "\n")
file.close()
updated_file = open('q9.txt')
print(updated_file.read())