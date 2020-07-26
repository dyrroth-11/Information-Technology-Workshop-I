#!/usr/bin/env python3
"""
Created on Wed Mar 25 08:29:04 2020

@author: Ashish Patel
"""
"""
#Write a Python program to convert an array to an ordinary list with the same items.

 LOGIC:1)we take a array as a input.
       2)Then convert it into a list using tolist() function.

"""
from array import * 
input_array = array('i' , list(map(int,input("Write the elements of the array:\n").split())))
list_of_array = input_array.tolist()

print(list_of_array)
