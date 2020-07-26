#!/usr/bin/env python3
"""
Created on Thu Apr 2 09:44:17 2020

@author: Ashish Patel
"""
"""
Write a Python program for binary search.

Example: Enter the sorted list of numbers: 3 5 10 12 15 20
The number to search for: 12
12 was found at index 3.

LOGIC:In this we search a sorted array by repeatedly dividing the search interval in half.
       Begin with an interval covering the whole array. If the value of the 
       search key is less than the item in the middle of the interval, narrow
       the interval to the lower half. Otherwise narrow it to the upper half.
       Repeatedly check until the value is found or the interval is empty.

 """
def binarySearch (a,start,end, x):
   if end >= start:
      mid = start + (end- start)//2
      if a[mid] == x: return mid
      elif a[mid] > x: return binarySearch(a, start, mid-1, x)
      else: return binarySearch(a, mid+1, end, x)
   else:
      return -1
a = list(map(int,input("Enter the elements of the list: \n").split()))
key = int(input("Enter the number to search for: \n"))
a=sorted(a)
ans = binarySearch(a, 0, len(a)-1, key)
if ans != -1:
   print ("{} was found at index {}.".format(key,ans))
else:
   print ("{} is not present" .format(key))