#!/usr/bin/env python3
"""
Created on Thu Apr 2 10:14:36 2020

@author: Ashish Patel
"""
"""
Write a Python program to sort a list of elements using the merge sort algorithm.

Example: Split Sample Data: [14, 46, 43, 27, 57, 41, 45, 21, 70]
Merge and Sort(Expected Result): [14, 21, 27, 41, 43, 45, 46, 57, 70]

 LOGIC: In this we keeps on dividing the list into equal halves until it 
        can no more be divided. By definition if it is only one element in
        the list, it is sorted. Then we combines the smaller sorted lists 
        keeping the new list sorted too.

 """
def mergeSort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        mergeSort(left)
        mergeSort(right)
        i,j,k = 0,0,0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

list = list(map(int,input("Please Enter the Elements of the list : \n").split()))
mergeSort(list)
print("The Sorted List is : ", list)
