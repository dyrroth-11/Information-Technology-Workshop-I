#!/usr/bin/env python3
"""
Created on Wed Mar 25 10:01:27 2020

@author: Ashish Patel
"""
"""
 Write a Python program to split a list every Nth element.
 
 Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']  n=3
 Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

 
 LOGIC:1)We take a list  as well a number n as input.
       2)Then make a new list of lists with the defination that ith element to be kept in i%n the list.
       3)Then finally printed the splited list. 
"""
input_list = list(input("Enter the first list: ").split(","))
n = int(input("Enter the value of n : "))
output_list = [input_list[i::n] for i in range(n)]

print(output_list)