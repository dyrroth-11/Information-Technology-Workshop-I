#!/usr/bin/env python3
"""
Created on Tue Apr 7 09:34:27 2020

@author: Ashish Patel
"""
"""
Write python program to get the file size of a text file in bytes.

Input: test.txt

Output: File size in bytes of a file test.txt is: 765

 """
import os
x = os.stat('test.txt')
print("File size in bytes of a plain file: "+str(x.st_size))