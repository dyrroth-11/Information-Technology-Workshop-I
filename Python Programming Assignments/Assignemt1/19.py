#!/usr/bin/env python3
"""
Created on Wed Mar 25 08:02:12 2020

@author: Ashish Patel
"""
"""
 Write a Python program to insert a given string at the beginning of all items in a list.
 
 Sample list : [1,2,3,4], string : emp
 Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
 
 LOGIC:1)we take list as well as string to be inserted as input.
       2)Then travers through the list and concatenate the given string in front of every element of the list.
       
"""
l = list(input("Enter a list: ").split(","))
s = str(input("Enter a string: "))
new_l=[]
for i in l:
    f=str(s+str(i))
    new_l.append(f)

print(new_l)