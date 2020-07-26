#!/usr/bin/env python3
"""
Created on Wed Mar 25 07:48:24 2020

@author: Ashish Patel
"""
"""
 Write a Python function to merge two sorted arrays.
 Sample Items :
 m=[1, 4, 8]
 n=[2, 3, 7]
 Expected Output: mn=[1, 2, 3, 4, 7, 8]

 LOGIC:1)we take two array of number as input.
       2)then merge them in a single one.
       3)Finally sorted the array and printed it.

"""
array1=list(input("Enter first array").split(" "))
array2=list(input("Enter second array").split(" "))
merge_array=array1+array2
merge_array.sort()
print(merge_array)