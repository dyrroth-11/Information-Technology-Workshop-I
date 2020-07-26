#!/usr/bin/env python3
"""
Created on Tue Apr 7 07:43:04 2020

@author: Ashish Patel
"""
"""
Write python program to append text to a file and display the text.

Input: Content of myfile.txt i.e. Hello everyone !

Output: Hello everyone !
        This is ITW1 class.

"""
file = open("myfile.txt", "a")
text=str(input("Enter the text which you want to append to it : "))
file.write('\n'+str(text))
file.close()
final_file = open("myfile.txt")
print(final_file.read())