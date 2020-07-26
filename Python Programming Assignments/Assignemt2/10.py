#!/usr/bin/env python3
"""
Created on Thu Apr 2 08:52:27 2020

@author: Ashish Patel
"""
"""
Write a Python program to make a chain of function decorators (bold, italic, underline etc.).

Example: Input: hello world 
         Output: hello world

LOGIC:In this we use chaining of functions as function decorators to transform 
      strings into bold , italic and underlined form.  

 """
def Bold(string):
    def wrapped():
        return "<b>" + string() + "</b>"
    return wrapped

def Italic(string):
    def wrapped():
        return "<i>" + string() + "</i>"
    return wrapped

def Underline(string):
    def wrapped():
        return "<u>" + string() + "</u>"
    return wrapped
istr = str(input("Enter a string : \n"))
@Bold
@Italic
@Underline

def chain(s=istr):
    return s
print(chain())
