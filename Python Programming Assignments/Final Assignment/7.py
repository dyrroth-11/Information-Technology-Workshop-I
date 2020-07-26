#!/usr/bin/env python3
"""
Created on Fri Jun 19 11:34:49 2020

@author: Ashish Patel
"""
"""
Question: From a given array A[] of positive integers of size N and a positive integer K, write 
		  a python code to find the maximum possible length of subarray which can be made equal 
		  by adding some integer value to each element of the sub-array such that the sum of the 
		  added elements does not exceed K.
Example
	Input: N = 5, A[] = {1, 4, 9, 3, 6}, K = 9
    Output: 3
Logic: In this we looped through all the possible subarray and make its all element equall and
       counted cnt that is the number of  element we need to add in and checked if cnt is less 
       that K we updated our answer if current subarray length is larger that current maximum.
"""
N = int(input("Enter the value of N : "))

arr = list(map(int,input("Enter the list of elements  (in space seperated form) : ").strip().split()))

K = int(input("Enter the value of K : "))

answer=0

for i in range(N):
    for j in range(i+1,N):
        mx = 0
        for k in range(i,j+1):
            mx = max(mx,arr[k])
        cnt = 0
        for k in range(i,j+1):
            cnt = cnt + abs(arr[k]-mx)
        if cnt <= K:
            answer = max(answer, j-i+1)

print(answer)