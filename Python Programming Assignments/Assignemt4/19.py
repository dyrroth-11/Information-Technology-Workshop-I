#!/usr/bin/env python3
"""
Created on Thu Apr 16 11:08:53 2020

@author: Ashish Patel
"""
"""
Write a Pandas program to get the first 3 rows of a given DataFrame.

Example: Input: Sample DataFrame from question 18.
         Output: First three rows of the data frame:
                 attempts name qualify score
                 a 1 Anastasia yes 12.5
                 b 3 Dima no 9.0
                 c 2 Katherine yes 16.5

"""

import pandas
import numpy

data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, numpy.nan, 9, 20, 14.5, numpy.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

dframe = pandas.DataFrame(data , index=labels)
print("First three rows of the data frame:")
print(dframe.iloc[:3])