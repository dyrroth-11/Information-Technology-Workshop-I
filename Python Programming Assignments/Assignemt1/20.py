#!/usr/bin/env python3
"""
Created on Wed Mar 25 09:28:02 2020

@author: Ashish Patel
"""
"""
 Write a Python program to compute the similarity between two lists.
 
 Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
 Expected Output:
 Color1-Color2: ['white', 'orange', 'red']
 Color2-Color1: ['black', 'yellow']
 
 LOGIC:1)we take two lists as input.
       2)Then used the set operation of taking difference by typecasting the list into set.
       3)finally printed the difference of lists. 
"""
list1 = list(input("Enter the first list: ").split(","))
list2 = list(input("Enter the second list: ").split(","))
print("list1 - list2: " + str(",".join(list(set(list1)-set(list2)))))
print("list2 - list1: " + str(",".join(list(set(list2)-set(list1)))))