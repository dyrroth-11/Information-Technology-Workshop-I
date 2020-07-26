#!/usr/bin/env python3
"""
Created on Thu Apr 16 07:53:04 2020

@author: Ashish Patel
"""
"""
Write a python class to access a member through a super and parent class name.

"""
class IIT(object):
  def __init__(self, iit_name):
    print(iit_name, 'is one of the best college in india.')
    
class IIT_BHU(IIT):
  def __init__(self):
    print('It is the best IIT.')
    super().__init__('IIT_BHU')
    
x = IIT_BHU()