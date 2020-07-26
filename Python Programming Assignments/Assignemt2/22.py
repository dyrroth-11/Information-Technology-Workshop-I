#!/usr/bin/env python3
"""
Created on Thu Apr 2 11:37:26 2020

@author: Ashish Patel
"""
"""
Generate three random password string of length 10 with special characters, letters, and digits by
using python modules (random and string).

Example: First Random String: yrjmcyi^VS
         Second Random String: |}Hd]!^>~l
         Third Random String: 3^a93@x=|Z

LOGIC: In this we defined a function which use string methods ascii_letters,
       digits and punctuation and random to choice 10 charcaters randomly 
       from these ascii letters, digits and punctuations to generate a random
       string of length 10.

 """
import random
import string
def pgen():
    password = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password) for i in range(10))

print ("First Random String: ",pgen())
print ("Second Random String: ",pgen())
print ("Third Random String: ",pgen())