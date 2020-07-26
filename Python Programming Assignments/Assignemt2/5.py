#!/usr/bin/env python3
"""
Created on Thu Apr 2 07:51:35 2020

@author: Ashish Patel
"""
"""
Write a Python program to remove an empty tuple(s) from a list of tuples.

Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

LOGIC:In this we traverse through the list and check for every element if it
      is a tuple or not, and if it is a tuple we added at to a new list. 

 """
def Empty_Remove(list_tuple):
    list_tuple = [x for x in list_tuple if x]
    return list_tuple

list_tuple =  [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(Empty_Remove(list_tuple))