#!/usr/bin/env python3
"""
Created on Wed Mar 25 07:28:22 2020

@author: Ashish Patel
"""
"""
#Write a Python program to sort a string lexicographically.
sample input: it is a good day
output: a day good it is 

LOGIC:1)First we take a string with multiple words as input.
      2)Then splited it into words.
      3)Then sorted the list of words and printed it.
"""
s = str(input("Enter a string"))
words_s = s.split()
words_s.sort()
for i in words_s:
    print(i + " ",end='')

