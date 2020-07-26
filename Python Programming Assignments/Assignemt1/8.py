#!/usr/bin/env python3
"""
Created on Wed Mar 25 07:41:14 2020

@author: Ashish Patel
"""
"""
 Write a Python function that accepts a hyphen-separated sequence of words as input and prints the
 words in a hyphen-separated sequence after sorting them alphabetically.
 Sample Items : green-red-yellow-black-white
 Expected Result : black-green-red-white-yellow

 LOGIC:1)we splitted hyphen separated string int a list of words.
       2)Then sorted the list and printed the words with hypen between them.  

"""
words = list(input("Enter a hyphen separated string: ").split('-'))
words.sort()
print("-".join(words))