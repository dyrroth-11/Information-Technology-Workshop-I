#!/usr/bin/env python3
"""
Created on Wed Mar 25 07:22:31 2020

@author: Ashish Patel
"""
"""
Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

LOGIC: 1)First we take 2 strings as input.
       2)Then find the mid_index of first string.
       3)Then concatenated string2 after string1's substring from index 0 to mid .
       4)Finally concatenated remaning part of string1 after string2.
"""
s1=str(input("Enter first string"))
s2=str(input("Enter second string"))

def insert_string_middle(string1,string2):
    mid_index = len(string1)//2
    return string1[:mid_index+1] + string2 + string1[mid_index + 1:]

print(insert_string_middle(s1,s2))
