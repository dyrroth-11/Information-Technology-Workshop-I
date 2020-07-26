#!/usr/bin/env python3
"""
Created on Thu Apr 2 10:49:02 2020

@author: Ashish Patel
"""
"""
Define a function reverse() that computes the reversal of a string.

For example, reverse(“I am testing”) should return the string ”gnitset ma I”.

LOGIC:In this we take a string as input and define a empty string rev_string
      then iterated through the characters of the string and concatenated them
      in front of the rev_string, finally printed the rev_string.

 """
input_string = str(input("Enter a string : \n"))
rev_string=''
for x in input_string:
    rev_string = x + rev_string

print("Reversed string is: " + rev_string)
