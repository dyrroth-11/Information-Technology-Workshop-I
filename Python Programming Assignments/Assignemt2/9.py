#!/usr/bin/env python3
"""
Created on Thu Apr 2 08:34:52 2020

@author: Ashish Patel
"""
"""
Write a Python program to create set difference, union, and intersection of sets.

Example: Input: set(["green", "blue"]), set(["blue", "yellow"])
         Output: Difference: {'blue'}, {'green'} 
                 Union: {'yellow', 'green', 'blue'}
                 Intersection: {'blue'}

 LOGIC: In this we take 2 set of numbers as input and use the properties of 
        difference, union and intersection of set to find the values of difference ,
        union and intersection of these sets. 

 """
set1 = set(input("Enter elements of first set: \n").split())
set2 = set(input("Enter elements of second set:\n ").split())

print("Difference: {},{}".format(set1 - (set1 & set2 ), set2 - (set1 & set2)))
print("Union: {}".format(set1 | set2))
print("Intersection: {}".format(set1 & set2))