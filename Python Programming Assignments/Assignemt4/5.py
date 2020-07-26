#!/usr/bin/env python3
"""
Created on Thu Apr 16 08:06:17 2020

@author: Ashish Patel
"""
"""
Write a Python class named Rectangle, constructed by a length and width and a method that will
compute the area of the rectangle.

"""
class rectangle:

	def __init__(self,length,width):
		self.length = length
		self.width = width

	def area(self):
		print(self.length*self.width)

l = int(input("Length : \n"))
b = int(input("Breadth : \n"))

R = rectangle(l,b)
print("Area :")
R.area()