#!/usr/bin/env python3
"""
Created on Thu Apr 2 09:56:34 2020

@author: Ashish Patel
"""
"""
Write a Python program to sort a list of elements using the bubble sort algorithm.

Example: Sample Data: [14, 46, 43, 27, 57, 41, 45, 21, 70]
Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70]

LOGIC:In this we  implemented a sorting algorithm which is comparison-based 
      algorithm in which each pair of adjacent elements is compared and the 
      elements are swapped if they are not in order.

 """
list = list(map(int,input("Please Enter the Elements of the list : \n").split()))
for i in range(len(list)-1):
    for j in range(len(list) -i -2):
        if(list[j] > list[j + 1]):
            list[j], list[j+1] = list[j+1], list[j]

print("The Sorted List is : ", list)