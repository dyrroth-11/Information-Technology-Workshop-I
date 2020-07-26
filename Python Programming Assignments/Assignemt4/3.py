#!/usr/bin/env python3
"""
Created on Thu Apr 16 07:47:12 2020

@author: Ashish Patel
"""
"""
Write a python class to check if a class is a subclass of another class or not.

"""


class Super:
    pass
class Child(Super):
    pass
class GrandChild(Child):
    pass

class check:

	def __init__(self , c1 , c2):
		self.c1 = c1
		self.c2 = c2

	def checkIt(self):
		print(issubclass(self.c1,self.c2))


obj = check(Child,GrandChild)

obj.checkIt()