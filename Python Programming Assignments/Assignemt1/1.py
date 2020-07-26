#!/usr/bin/env python3
"""
Created on Wed Mar 25 07:03:48 2020

@author: Ashish Patel
"""
"""
 Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
 if the string length is less than 2, return instead of the empty string.

 Sample String : 'a1resource'
 Expected Result : 'a1ce'
 Sample String : 'a1'
 Expected Result : 'a1a1'
 Sample String : ' a'
 Expected Result : Empty String 

 LOGIC:1)we take a string as input.
       2)if the length of the string is less than 2 we printed an empty string.
       3)Else printed first and last two character of the string.
"""
s=str(input("Enter a string : "))
n=len(s)
if n < 2:
	print("")
else:
	print(s[0:2]+s[-2:])