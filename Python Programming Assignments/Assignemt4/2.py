#!/usr/bin/env python3
"""
Created on Thu Apr 16 07:32:31 2020

@author: Ashish Patel
"""
"""
Write a python class to convert Hexadecimal to Decimal using class creation.

Example: Input Hexadecimal: C77, 
         Output Decimal: 3191

"""
class hex_to_dec:

	def __init__(self,hexr):
		self.hexr = hexr
		self.decr = int(str(hexr),16)

s = str(input("Enter a Hexadecimal number :\n"))
obj = hex_to_dec(s)
print(obj.decr)