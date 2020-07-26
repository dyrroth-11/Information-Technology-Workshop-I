#!/usr/bin/env python3
"""
Created on Thu Apr 2 07:21:48 2020

@author: Ashish Patel
"""
"""
Write a Python program to match key values in two dictionaries.

Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y.

LOGIC: In this we iterate through both the dictionaries and find if 
       particular element belong to both, if so we print that element.

 """
first_dict = {'key1': 1, 'key2': 3, 'key3': 2,'key4': 5 }
second_dict = {'key1': 1, 'key2': 2, 'key3': 4, 'key4': 5}
for (i,j) in set(first_dict.items()) & set(second_dict.items()):
    print('%s: %s is present in both  dictionaries ' % (i,j))