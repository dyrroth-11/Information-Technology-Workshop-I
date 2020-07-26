#!/usr/bin/env python3
"""
Created on Wed Mar 25 11:21:07 2020

@author: Ashish Patel
"""
"""
 Write a Python program to remove duplicates from a list of lists.
 
 Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
 New List : [[10, 20], [30, 56, 25], [33], [40]]
 
 LOGIC:1)We created a empty list.
       2)then traverse through the elements of the original list if the same elements is present in the new list we continue else append the element in new list.
       3)finally print the new list contaning no duplicate list.
"""
input_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
final_list = []

for i in input_list:
    if i not in final_list:
        final_list.append(i)

print(final_list)