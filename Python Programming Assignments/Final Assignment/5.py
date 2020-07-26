#!/usr/bin/env python3
"""
Created on Fri Jun 19 10:56:02 2020

@author: Ashish Patel
"""
"""
Question: Write a python program using functions that ask the user for an integer “N” as input 
		  and print an alphabet rangoli of size “N”.
Example
	Input: 3
    Output:		 c
			   c b c
			 c b a b c
			   c b c
				 c
Logic: We initally store all the alphabets in a list. Then we define two fuction one which print 
	   our pattern and other which return a list of index of character we need to use. In print
	   function we called string list function to get a list of all index of charcter we have to 
	   print in current line then finally make a string by joining those character and printing 
	   that string .
"""
letterString=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def stringlist(N):
    return list(range(N))+list(range(N-2,-1,-1))

def printRangoli(N):
    for i in stringlist(N):
        print(' '.join([letterString[N - j - 1] for j in stringlist(i + 1)]).center(4 * (N - 1) + 1, ' '))

N = int(input("Enter the value of N :"))

printRangoli(N)