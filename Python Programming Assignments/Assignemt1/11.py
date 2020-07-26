#!/usr/bin/env python3
"""
Created on Wed Mar 25 08:02:12 2020

@author: Ashish Patel
"""
"""
 Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as
 its input and print the numbers that are divisible by 5 in a comma separated sequence.
 
 Sample Data : 0100,0011,1010,1001,1100,1001
 Expected Output : 1010

 LOGIC:1)we take all the input binaray numbers in a list.
       2)Then traverse through the list and checked every numbr if it is divisible by 5.
       3)if so printed the number else move to next number.

"""
num_list = list(input("Enter four numbers:").split(','))
num_div_5=[]
for i in num_list:
    t=int(i,2)
    if t%5 == 0:
        num_div_5.append(i)

print(",".join(num_div_5))