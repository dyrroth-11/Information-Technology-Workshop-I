#!/usr/bin/env python3
"""
Created on Wed Mar 25 08:18:28 2020

@author: Ashish Patel
"""
"""
 Write a Python program to remove a specified item using the index from an array.
 
 LOGIC:1)we have taken array as well as the index of number to be removed as input.
       2)then used pop() function to remove the element at given index 

"""

input_array = input("Write the elements of the array:\n").split()
index = int(input("Enter the index to be removed: "))
input_array.pop(index)

print(input_array)
