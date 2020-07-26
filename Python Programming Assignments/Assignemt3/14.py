#!/usr/bin/env python3
"""
Created on Tue Apr 7 11:27:48 2020

@author: Ashish Patel
"""
"""
Write python code to find the current working directory also do the following operations:
A. creating a new directory.
B. create a new text file in the new directory.
C. delete the new directory.

Example: My current working directory: '/home/randheer/ML/File input-output'
         A. Create a new folder in my current working directory named as “newdir”
         B. In newdir, write a text file as “myfile.txt”
         C. Delete the “newdir”

 """
import os
import shutil

# current directory
pwd = os.getcwd()
print ("The current working directory is " + str(pwd))

# A. creating a new directory.
new_dir_path = os.path.join(pwd,"newdir")
os.mkdir(new_dir_path)

# B. create a new text file in the new directory.
file = open(os.path.join(new_dir_path,"my.txt"),'wb')
print(new_dir_path)
file.close()

#  C. delete the new directory.
shutil.rmtree(new_dir_path)