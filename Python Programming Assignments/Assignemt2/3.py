#!/usr/bin/env python3
"""
Created on Thu Apr 2 07:38:27 2020

@author: Ashish Patel
"""
"""
Write a Python program to replace dictionary values with their sum.

Example: Input: {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI': 82},
                {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
                {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
         Output: [{'subject': 'math', 'id': 1, 'V+VI': 76.0},
                  {'subject': 'math', 'id': 2, 'V+VI': 73.5}
                  {'subject': 'math', 'id': 3, 'V+VI': 80.5}]

LOGIC: We iterate through the list of dictionaries and store the value of 
       elements with key 'V' and 'VI' and then add an element with key 'V + VI'
       and value as sum of previous stored values.

 """
list= [
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]
for i in list:
    x = i.pop('V')
    y = i.pop('VI')
    i['V+VI'] = (x+y)/2

print(list)
