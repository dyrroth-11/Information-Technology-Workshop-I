#!/usr/bin/env python3
"""
Created on Thu Apr 16 12:51:27 2020

@author: Ashish Patel
"""
"""
Write a python program to handle exception error using try and except, else, finally, and raise within a single
program.

"""

x=0
if x<0:
    raise Exception("Sorry, no numbers below zero")
try:
  print(x)
except:
  print("Something went wrong")
else:
  print("Else statement")
finally:
  print("The 'try except' is finished")