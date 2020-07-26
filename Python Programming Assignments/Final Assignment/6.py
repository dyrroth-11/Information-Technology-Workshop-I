#!/usr/bin/env python3
"""
Created on Fri Jun 19 11:14:27 2020

@author: Ashish Patel
"""
"""
Question: Write a python program using functions that ask the user for a positive integer “N” 
		  as input and print a numerical triangle of height “N-1” like the one below:
Example
	Input: 5 
    Output: 1
			2 2
			3 3 3
			4 4 4 4
Logic: We defined a printNumericalTriangle function which print all numbers i from 1 to n-1 i times
	   in seperate lines starting from x =1 to x=n-1.
"""
def printNumericalTriangle(n):
    x = 1
    for i in range(n-1):
        for j in range(x):
            print(x , end=" ")
        print("")
        x += 1

N = int(input("Enter the value of N : "))

printNumericalTriangle(N)