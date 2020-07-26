#!/usr/bin/env python3
"""
Created on Fri Jun 19 09:37:12 2020

@author: Ashish Patel
"""
"""
Question: Write a python program using functions that asks the user for a long string 
		  containing multiple words. Print back the user string, except with the words 
		  in backward order.
Example
	Input: This is ITW1 2020 
    Output: 2020 ITW1 is This
Logic:
	Here we defined a function rev_string which take a string as input and split int into words
	and store those words in wordsList then finally join all those words in reverse order into 
	a string and return that string.
"""
def rev_string(string):

    wordsList = string.split(' ')
    backwordString = (' ').join(reversed(wordsList))
    return backwordString


inputString = str(input("Enter a string : "))
reversedString = rev_string(inputString)
print(reversedString)