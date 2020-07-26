#!/usr/bin/env python3
"""
Created on Thu Apr 2 08:05:21 2020

@author: Ashish Patel
"""
"""
Write a Python program to count the elements in a list until an element is a tuple.

Example: Input: [10,20,30,(10,20),40]
         Output: 3

LOGIC:In this we iterate througth the list check if element is a tuple if 
      not, we increase count by 1 otherwise break the loop .finally print
      the value of count. 

 """
list= [10,20,30,(10,20),40]
count = 0
for i in list:
    if isinstance(i,tuple):
        break
    count = count + 1
print(count)