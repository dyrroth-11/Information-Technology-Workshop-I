#!/usr/bin/env python3
"""
Created on Thu Apr 2 11:08:46 2020

@author: Ashish Patel
"""
"""
Write a Python program to get the size of an object in bytes by using module “sys”.

Example: Memory size of 'one' = 28 bytes
         Memory size of 'four' = 29 bytes
         Memory size of 'three' = 30 bytes

LOGIC:In this we used the getsizeof() method of sys module to get the 
      size of variable objects in bytes. 

 """
import sys
a , b , c = "one", "four" , "three"
print("Memory size of '{}' = {} bytes".format(a,sys.getsizeof(a)))
print("Memory size of '{}' = {} bytes".format(b,sys.getsizeof(b)))
print("Memory size of '{}' = {} bytes".format(c,sys.getsizeof(c)))