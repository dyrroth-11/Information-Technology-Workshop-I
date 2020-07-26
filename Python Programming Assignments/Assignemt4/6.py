#!/usr/bin/env python3
"""
Created on Thu Apr 16 08:19:24 2020

@author: Ashish Patel
"""
"""
Write a Python class to reverse a string word by word.

Example: Input string: hello, 
         Output string: olleh

"""
class rev:

	def __init__(self,s):
		self.s = s

	def reverse(self):
		ans = self.s[::-1]
		return ans

in_string = str(input("Enter a string : \n"))
S = rev(in_string)
print(S.reverse())