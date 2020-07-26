#!/usr/bin/env python3
"""
Created on Tue Apr 7 08:22:04 2020

@author: Ashish Patel
"""
"""
 Convert the input file to the list of tuples and the list must contain atleast one empty tuple.
 The conversation is done at word level. Then remove all empty tuple(s) from the input list.

 Input: Content of file test.txt
 Output: [('W', 'h', 'a', 't'), ('i', 's'), ('P', 'y', 't', 'h', 'o', 'n')...............]
"""
def Empty_Remove(list_tuple):
    list_tuple = [x for x in list_tuple if x]
    return list_tuple

file = open('test.txt', 'r')
list_tuple = []
for line in file:
    for word in line.split():
        list_tuple.append(tuple(word))
        
print(Empty_Remove(list_tuple))