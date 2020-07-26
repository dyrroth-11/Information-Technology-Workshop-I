#!/usr/bin/env python3
"""
Created on Fri Jun 19 12:23:16 2020

@author: Ashish Patel
"""
"""
Question: Write a python program to create an 8x3 integer array from a range of 10 to 34 so that 
		  he difference between each element is 1 and then split the array into four equal-sized 
		  sub-arrays.

Logic: we used numpy inbuild function to create a 8*3 array with numner in range 10-34 and with
	   difference of 1 between elements. Then again we use numpy method split to divide our 8*3
	   array into 4 groups. 

"""
import numpy as np


def generateArray():
    print("######## 8x3 array ########\n")
    array8x3 = np.arange(10, 34, 1)
    array8x3 = array8x3.reshape(8, 3)
    print(array8x3)
    print("\n######## Sub Array List ########\n")
    subGroupList = np.split(array8x3, 4)
    print(subGroupList)


generateArray()


