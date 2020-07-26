#!/usr/bin/env python3
"""
Created on Thu Apr 2 10:02:28 2020

@author: Ashish Patel
"""
"""
Write a Python program to sort a list of elements using the selection sort algorithm.

Example: Sample Data: [14, 46, 43, 27, 57, 41, 45, 21, 70]
Expected Result: [14, 21, 27, 41, 43, 45, 46, 57, 70]

LOGIC: In this we implemented selection sort algorithm which is a in-place
       comparison-based algorithm in which the list is divided into two parts,
       the sorted part at the left end and the unsorted part at the right end.
       Initially, the sorted part is empty and the unsorted part is the entire
       list.The smallest element is selected from the unsorted array and swapped 
       with the leftmost element, and that element becomes a part of the sorted 
       array. This process continues moving unsorted array boundary by one element
       to the right.

 """
list = list(map(int,input("Please Enter the Elements of the list : \n").split()))
for i in range(len(list)):
   min_element_index= i
   for j in range(i+1, len(list)):
      if list[min_element_index] > list[j]:
         min_element_index = j
   list[i], list[min_element_index] = list[min_element_index], list[i]

print("The Sorted List is : ", list)