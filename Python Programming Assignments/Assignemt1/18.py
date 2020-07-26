#!/usr/bin/env python3
"""
Created on Wed Mar 25 09:12:24 2020

@author: Ashish Patel
"""
"""
 Write a Python program to find the list in a list of lists whose sum of elements is the highest.
 
 Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
 Expected Output: [10, 11, 12]
 
 LOGIC:1)we traverse through all the list and sum their element.
       2)if the sum is greater then maxmimin sum till now, maximum sum till now become current sum.
       3)and maximum sum list index is also stored.

"""
list_of_lists = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
i=0
max_list_index = 0
max_sum = 0
for list in list_of_lists:
    list_sum = 0
    for x in list:
        list_sum += x
        if list_sum > max_sum:
            max_sum = list_sum
            max_list_index = i
    i = i + 1

print(list_of_lists[max_list_index])