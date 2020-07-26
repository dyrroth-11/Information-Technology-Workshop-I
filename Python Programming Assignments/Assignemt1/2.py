#!/usr/bin/env python3
"""
Created on Wed Mar 25 23:20:27 2020

@author: Ashish patel
"""
"""
Write a Python program to get a string from a given string where all occurrences of its first char have
been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'

LOGIC: 1)stored first character in a temparary variable first_char.
       2)then replaced all occurrence of first_char with '$' using replace() function.
       3)After that printed first_char + input string form second index.
"""

s= str(input("Enter a string : "))
first_char=s[0]
s=s.replace(first_char,"$")
s=first_char + s[1:]
print(s)