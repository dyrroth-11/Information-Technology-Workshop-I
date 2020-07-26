#!/usr/bin/env python3
"""
Created on Thu Apr 2 09:27:02 2020

@author: Ashish Patel
"""
"""
Write a Python program of recursion list sum.
Test Data: [1, 2, [3,4], [5,6]]
Expected Result: 21

LOGIC:In this we defined a recursive function which iterate througth the list
      and if particular element is a list we call recursive for it otherwise 
      we increase the value of sum with the element.  

 """
def list_sum(list):
	sum = 0
	for x in list:
		if type(x) == type([]):
			sum += list_sum(x)
		else:
			sum += x
	return sum
list=[1,2,[3,4],[5,6]]
print("Result: " + str(list_sum(list)))