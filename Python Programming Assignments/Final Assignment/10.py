#!/usr/bin/env python3
"""
Created on Fri Jun 19 12:58:51 2020

@author: Ashish Patel
"""
"""
Question: Write a python program that accepts a string as input from the user to find the input 
		  string permutations.
Example
	Input: ABC 
    Output: ABC
			ACB
			BAC
			BCA
			CAB
			CBA
Logic: We defined a recursive function which append every character at every possible places
 	   and form all n factorial permuations of the input string when we reach n character in our 
 	   string i.e successfully created a possible permuation we print that.
"""
def makePermutations(charList,i,N):
    if i==N:
        print(''.join(charList) )
    else:
        for j in range(i, N):
            charList[i], charList[j] = charList[j], charList[i]
            makePermutations(charList, i+1, N)
            charList[i], charList[j] = charList[j], charList[i]


string = str(input("Enter a string : "))
n = len(string)
charList = list(string)
makePermutations(charList,0,n)