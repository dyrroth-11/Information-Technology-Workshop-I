#!/usr/bin/env python3
"""
Created on Fri Jun 19 12:41:07 2020

@author: Ashish Patel
"""
"""
Question: Write a python program that accepts input from the user and checks whether the input 
		  is a palindrome or not.
Example
	Input: Malayalam 
    Output: true
Logic:Here we iterate mid way through the string and checked for every element if it match with 
      its corresponding element from the end if not so we just changed our flag to false. 

"""
string = str(input("Enter a string : "))
n = len(string)
ispalindrome = True
for i in range(int(n/2)):
    if string[i] != string[n-i-1]:
        ispalindrome = False
        break

if ispalindrome:
    print("true")
else :
    print("false")
