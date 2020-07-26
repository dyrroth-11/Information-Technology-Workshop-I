#!/usr/bin/env python3
"""
Created on Wed Mar 25 08:14:32 2020

@author: Ashish Patel
"""
"""
 Write a Python program to get the number of occurrences of a specified element in an array

 LOGIC:1)We had just taken array and number whos occurence is to be calculated as input.
       2)Then used the count() function to calculate its occurence.

"""
from array import *
input_array = array('i' , [1,3,3,4,7,7,8,9,4,4,5,7,9] )
n = int(input("Enter a number whos number of occurrences is to be calculated : "))

print(input_array.count(n))
