#!/usr/bin/env python3
"""
Created on Wed Mar 25 07:57:08 2020

@author: Ashish Patel
"""
"""
 Write a Python function that accepts a string and calculate the number of upper case letters and
 lower case letters.
 Sample String : 'The quick Brow Fox'
 Expected Output :
 No. of Upper case characters : 3
 No. of Lower case Characters : 12

 LOGIC:1)we traverse through the input string and checked for every character.
       2)If it is upper case we inceresed upper_counter by 1 else if it is lower case we increased lower_counter by 1.
       3)finally printed the number of upper and lower case letters.

"""
import string
string = str(input("Enter a string:"))
upper = 0
lower = 0
for i in string:
    if i.isupper(): upper =upper +1
    elif i.islower(): lower = lower +1
print("No. of Upper case characters : {}".format(upper))
print("No. of Lower case characters : {}".format(lower))