#!/usr/bin/env python3
"""
Created on Thu Apr 16 11:47:22 2020

@author: Ashish Patel
"""
"""
Write a Pandas program to select the rows where the score is between 15 and 20 (inclusive).

Example: Input: Sample DataFrame_1 from question 20.
         Output: Rows where score between 15 and 20 (inclusive):
                 attempts name qualify score
                 c 2 Katherine yes 16.5
                 f 3 Michael yes 20.0
                 j 1 Jonas yes 19.0

"""

import pandas
import numpy
data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, numpy.nan, 9, 20, 14.5, numpy.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

dframe = pandas.DataFrame(data ,index=labels)
print("Rows where score between 15 and 20 (inclusive):")
print(dframe[dframe['score'].between(15, 20)])