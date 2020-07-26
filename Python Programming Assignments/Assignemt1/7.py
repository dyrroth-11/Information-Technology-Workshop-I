#!/usr/bin/env python3
"""
Created on Wed Mar 25 07:34:41 2020

@author: Ashish Patel
"""
"""
# Write a Python function that prints out the first ‘n’ rows of Pascal's triangle. ‘n’ is user input.

LOGIC:1)As we know pascals triange consist of the binomial coefficient of (1+x)^(n-1) for nth row.
      2)Therefore we computed coefficent and printed then in the order that we are suppose to do.

"""
def NCR(n, r):
    x = 1
    if (r > n - r):
        r = n - r
    for i in range(r):
        x = x * (n - i)
        x = x // (i + 1)

    return x

def Pascal_triangle(n):
    y=2*(n-1)
    for x in range(n):
        for j in range(y):
            print(" ",end="")
        for i in range(x + 1):
            print(NCR(x, i),
                  " ", end="")
        print()
        y=y-2

n=int(input("Enter number of rows of Pascal's triangle to be printed: "))

Pascal_triangle(n)