#!/usr/bin/env python3
"""
Created on Thu Apr 16 10:52:16 2020

@author: Ashish Patel
"""
"""
Write a Pandas program to create and display a DataFrame from a specified dictionary data which
has the index labels.

Sample DataFrame:
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin','Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Output:
attempts name qualify score
a 1 Anastasia yes 12.5
b 3 Dima no 9.0
c 2 Katherine yes 16.5
d 3 James no NaN
e 2 Emily no 9.0
f 3 Michael yes 20.0
g 1 Matthew yes 14.5
h 1 Laura no NaN
i 2 Kevin no 8.0
j 1 Jonas yes 19.0

"""

import pandas
import numpy

data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, numpy.nan, 9, 20, 14.5, numpy.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

dframe = pandas.DataFrame(data , index=labels)
print(dframe)