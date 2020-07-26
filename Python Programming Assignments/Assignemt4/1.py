#!/usr/bin/env python3
"""
Created on Thu Apr 16 07:21:48 2020

@author: Ashish Patel
"""
"""
Write a python class to show how we can change the class variable in python. Also, write a code to create an
empty class.

"""
# varaible changing in class:

class student:
	branch = "CSE-Btech"
	def __init__(self, name, roll): 
		self.name = name
		self.roll = roll

a=student("random",19000000)
print("initial branch variable : ", a.branch)

student.branch="CSE-IDD"

print("branch varible after changing : ",a.branch)

#creation of empty class

class empty:
	pass