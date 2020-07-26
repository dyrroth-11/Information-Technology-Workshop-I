#!/usr/bin/env python3
"""
Created on Fri Jun 19 10:22:12 2020

@author: Ashish Patel
"""
"""
Question: Write a python program using a given string “S” and width “W” to wrap the string “S” 
		  into a wordof width “W”. Also, print the first and last character of each word in a 
		  string of two characters. 
Example
	Input: S : ABCDEFGHIJKL
		   W : 4
	Output: Output_1:ABCD Output_2: AD
					 EFGH           EH
					 IJKL 			IL
Logic: Here we slice our string s into substing of size w by using makeSlice function which return
	   list of all those substring .Finally we output those substtring as we as their first and
	   last character.
"""
def makeSlice(s, w):
    return [s[i:i + w] for i in range(0, len(s), w)]

s = str(input("Enter string S : "))
w = int(input("Enter width W : "))

listOfSlices = makeSlice(s,w)
print("Output_1 :")
for i in listOfSlices:
    print(i)

print("Output_2 :")
for i  in listOfSlices:
    print(i[0],i[-1])