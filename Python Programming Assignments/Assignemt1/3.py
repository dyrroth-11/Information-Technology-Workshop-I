#!/usr/bin/env python3
"""
Created on Wed Mar 25 07:15:48 2020

@author: Ashish Patel
"""
"""
Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given
string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the
resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
LOGIC: 1)we find index of substring 'not' and 'poor'.
       2)Then check if poor_index > not_index if so replace the in between substring by 'good'.
       3)If not just printed the original string.
"""
s=str(input("Enter a string : "))
not_index = s.find("not")
poor_index = s.find("poor")
if not_index > 0 and poor_index > 0 and poor_index > not_index:
    s = s.replace(s[not_index: poor_index+4], "good")
print(s)