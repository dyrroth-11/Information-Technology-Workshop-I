#!/usr/bin/env python3
"""
Created on Thu Apr 2 07:27:08 2020

@author: Ashish Patel
"""
"""
Write a Python program to create a dictionary from two lists without losing duplicate values.

Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: defaultdict(<class 'set'>, {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3},
                 'Class-V': {1}})

LOGIC: In this we traverse in both the list and zip ith element from both list
       as a key value pair in a dictionary.

 """
from collections import defaultdict
list_1 = list(input("Enter first list : \n").split())
list_2 = list(input("Enter second list : \n").split())
ans = defaultdict(set)
for c, i in zip(list_1,list_2):
    ans[c].add(i)
print(ans)

