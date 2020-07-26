#!/usr/bin/env python3
"""
Created on Wed Mar 25 07:34:41 2020

@author: Ashish Patel
"""
"""
Write a Python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2

LOGIC:1)We decleared a alphabets string and the travesed through it's elements.
      2)Then counted the character's occurence in the input string if count > 1 this means it is repeted.
      3)Then printed the character with its count.
"""
string = str(input("Enter a string: "))
alphabets = "abcdefghijklmnopqrstuvwxyz"
for i in alphabets:
    if string.count(i) > 1:
        print("{0} {1}".format(i,string.count(i)))
