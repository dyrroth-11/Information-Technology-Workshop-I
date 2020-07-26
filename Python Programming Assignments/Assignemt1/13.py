#!/usr/bin/env python3
"""
Created on Wed Mar 25 08:02:12 2020

@author: Ashish Patel
"""
"""
 Write a Python program to print alphabet pattern 'R'.
 Expected Output:
 ****
 *  *
 *  *
 ****
 * *
 *  *

 LOGIC:1)first we analyse the dimensions of 'R' given in input.
       2)Then we looped for the rows of R i.e 7 and printed '*' according to the dimensions.

"""
R=""
for x in range(0,7):
    for y in range(0,7):
        if (y==1 or ((x==0 or x==3) and y>1 and y<5) or (y==5 and x!=0 and x<3) or (y==x-1 and x>2)):
            R = R + "*"
        else:
            R = R + " "
    R = R + "\n"
print(R)

     
"""
Alternate solution:
for x in range(7):
    if x==0 or x==3:
        print("****")
    elif x==4:
        print("**")
    elif x==5:
        print("* *")
    else:
        print("*  *")

"""