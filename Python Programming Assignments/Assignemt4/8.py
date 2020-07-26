#!/usr/bin/env python3
"""
Created on Thu Apr 16 08:43:14 2020

@author: Ashish Patel
"""
"""
Write a Python class to find a pair of elements (indices of the two numbers) from a given array
whose sum equals a specific target number.

Example: Input: Numbers: [10,20,10,40,50,60,70], target=50, 
         Output: 3, 4

"""
class target_sum:

	def __init__(self,arr,x):
		self.ls = arr
		self.n = len(self.ls)
		self.tgt = x

	def process(self):
		for i in range(self.n):
			for j in range(i+1,self.n,1):
				if arr[i] + arr[j] == self.tgt:
					return i,j

		return -1,-1

n = int(input())
print("Enter the elements of the array ")	
arr = []
for i in range(n):
	x = int(input())
	arr.append(x);

target = int(input("Enter the target number : "))
obj = target_sum(arr,target)
x,y = obj.process()

if x==-1 and y==-1:
	print("No pair found")
else:
	print(x+1,y+1)