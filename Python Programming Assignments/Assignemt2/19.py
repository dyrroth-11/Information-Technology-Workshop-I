#!/usr/bin/env python3
"""
Created on Thu Apr 2 10:54:19 2020

@author: Ashish Patel
"""
"""
Write a Python program to find the available built-in modules.

Example: math, random, uuid, sys, syslog etc.

LOGIC: In this we used inbuild builtin_module_names method of sys module
       to get the names of all the built in module and stored then in a list
       finally printed that list.

 """
import sys
list_module = sys.builtin_module_names
for x in list_module:
    print(x)