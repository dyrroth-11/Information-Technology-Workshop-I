#!/usr/bin/env python3
"""
Created on Wed Mar 25 11:16:03 2020

@author: Ashish Patel
"""
"""
 Write a Python program to iterate over two lists simultaneously.

 LOGIC:1)we take two list as input.
       2)Then traverse through both the list and used zip() method to print the pair.
       
"""
list1 = list(input("Enter first list: ").split(","))
list2 = list(input("Enter second list: ").split(","))

for (i,j) in zip(list1,list2):
    print(i,j)