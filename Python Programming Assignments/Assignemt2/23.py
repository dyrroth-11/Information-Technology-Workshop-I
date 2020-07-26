#!/usr/bin/env python3
"""
Created on Thu Apr 2 11:46:12 2020

@author: Ashish Patel
"""
"""
Write a python code using module “uuid” to generate universally unique secure randon string id of
length 8.

Example: random string using a UUID module is: 9C8E13FF

LOGIC: In this we used inbuilt uuid4() method of uuid module to generate 
       string id of length 8.

 """
import uuid
randomString = uuid.uuid4().hex
randomString = randomString.upper()[0:8]
print("random string using a UUID module is ",randomString )
