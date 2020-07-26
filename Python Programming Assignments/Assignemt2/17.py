#!/usr/bin/env python3
"""
Created on Thu Apr 2 10:36:12 2020

@author: Ashish Patel
"""
"""
Write a Python program using functions that asks the user for a long string containing multiple
words. Print back to the user the same string, except with the words in backwards order.

For example Input: My name is Michele
            Output: Michele is name My

 LOGIC:In this we take words of the string as element of a list and then 
       reversed the list of words using reverse() method .Then finally 
       constructed a rev_string but iterating through elements of the list
       and concatenating them into the rev_string.

 """
string_list = list(map(str,input("Enter a string of words : \n").split()))
string_list.reverse()
rev_string=''
for x in string_list:
    rev_string += x +' '
print(rev_string)
