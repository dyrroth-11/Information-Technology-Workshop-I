#!/usr/bin/env python3
"""
Created on Thu Apr 2 07:45:14 2020

@author: Ashish Patel
"""
"""
Write a Python program to sort a tuple by its float element.

Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

 LOGIC: In this we sorted the list of tuples according to second element i.e
        float values in reverse order (Decreasing order). 

 """
def Float_Sort(list):
    return (sorted(list, key=lambda x: float(x[1]), reverse=True))

list = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(Float_Sort(list))