#!/usr/bin/env python3
"""
Created on Fri Jun 19 10:06:42 2020

@author: Ashish Patel
"""
"""
Question: Write a python program that accepts multiple sensntences as input and prints 
		  the sentences afterconverting all the characters into captial letters in the 
		  sentences. 
Example
	Input: Hello students
		   Good luck for your examinations 
    Output: HELLO STUDENTS
			GOOD LUCK FOR YOUR EXAMINATIONS
Logic: Here we have a while loop which only terminate when we don't get any input string
	   when we get a string we transform it into upper text and print that.
"""
while True:
    line = str(input())
    if line:
        print(line.upper())
    else:
        break;
