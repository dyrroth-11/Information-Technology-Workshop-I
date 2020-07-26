#!/usr/bin/env python3
"""
Created on Tue Apr 7 10:32:24 2020

@author: Ashish Patel
"""
"""
Write python program that accepts sequence of lines as input and prints the lines after making all
characters in the sentence capitalized.

Input: Hello everyone
       Practice makes perfect
Output: HELLO EVERYONE
        PRACTICE MAKES PERFECT

"""
text = []
while 1:
    line = str(input())
    if line : text.append(line.upper())
    else: break
for line in text:
    print(line)