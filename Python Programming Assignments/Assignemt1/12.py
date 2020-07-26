#!/usr/bin/env python3
"""
Created on Wed Mar 25 08:02:12 2020

@author: Ashish Patel
"""
"""
 Write a Python program to insert a new item before the second element in an existing array.

 LOGIC:1)Take a array and number to be inserted  as input .
       2)Then inserted number before second element using insert() function.
       3)Finally printed the new array.

"""
from array import *
input_array = array('i' , [1,3,4,7,8,9,5,7,9] )
n = int(input("Enter a number to be inserted : "))
input_array.insert(1,n)
print(input_array)
