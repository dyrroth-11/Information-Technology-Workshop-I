#!/usr/bin/env python3
"""
Created on Fri Jun 19 09:12:37 2020

@author: Ashish Patel
"""
"""
Question: Write a python program to sort a list of elements using the quick sort algorithm.
Example
    Input: [10, 80, 30, 90, 40, 50, 70] 

    Output: [10, 30, 40, 50, 70, 80, 90]
Logic:
     It is a divide-and-conquer algo based on the idea of choosing one element as a 
     pivot element and partitioning the array around it such that left side of pivot 
     contains all the elements that are less than the pivot element  and right side 
     contains all elements greater than the pivot
"""
def quicksort(list):
    if len(list) == 1 or len(list) == 0:
        return list
    else:
        pivot = list[0]
        i = 0
        for j in range(len(list)-1):
            if list[j+1] < pivot:
                list[j+1],list[i+1] = list[i+1], list[j+1]
                i += 1
        list[0],list[i] = list[i],list[0]
        first_half = quicksort(list[:i])
        second_half = quicksort(list[i+1:])
        first_half.append(list[i])
        return first_half + second_half

element_list = list(map(int,input("Enter the list of elements  (in space seperated form) : ").strip().split()))

print(quicksort(element_list))