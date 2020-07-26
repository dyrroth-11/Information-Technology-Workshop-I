#!/usr/bin/env python3
"""
Created on Thu Apr 16 08:30:42 2020

@author: Ashish Patel
"""
"""
Write a Python class to find the three elements from a given array whose sum is zero.

Example: Input array : [-25, -10, -7, -3, 2, 4, 8, 10], 
         Output : [[-10, 2, 8], [-7, -3, 10]]

"""
class Sum_zero:

	def __init__(self,ls):
		self.arr = arr
		self.n = len(self.arr)

	def process(self):
		ans = []
		for i in range(self.n):
			for j in range(i+1,self.n,1):
				for k in range(j+1,self.n,1):
					if arr[i] + arr[j] + arr[k] == 0:
						temp = []
						temp.append(arr[i])
						temp.append(arr[j])
						temp.append(arr[k])
						ans.append(temp)
		return ans

n = int(input())
print("Enter the elements of the array : \n")
arr = []

for i in range(n):
	x = int(input())
	arr.append(x);

obj = Sum_zero(arr)
print("Output:")
print(obj.process())