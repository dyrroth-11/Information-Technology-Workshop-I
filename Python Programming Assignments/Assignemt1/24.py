#!/usr/bin/env python3
"""
Created on Wed Mar 25 11:21:07 2020

@author: Ashish Patel
"""
"""
 Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
 
 Sample list : ['p', 'q']
 n =5
 Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

 LOGIC:1)we take list and numner n as input.
       2)Then iterate in range (1,n) and concatenate it with every element of the list.
       3)finally print all the new elements.
"""
input_list = list(input("Enter  list: ").split(","))
n = int(input("Enter the value of n : "))
final_list = ['{}{}'.format(i,j) for j in range(1,n+1) for i in input_list ]
print(final_list)