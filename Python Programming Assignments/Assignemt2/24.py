#!/usr/bin/env python3
"""
Created on Thu Apr 2 11:58:13 2020

@author: Ashish Patel
"""
"""
Write a python code using module “random” to generate a 100 Lottery tickets and pick two lucky
tickets from it as a winner.
Note: You must adhere to the following conditions:
1. Lottery number must be 10 digits long.
2. All 100 ticket number must be unique.

Example: Creating 100 random lottery tickets
         Lucky 2 lottery tickets are [7184805696, 7380986204]

LOGIC:In this we randrange() method of random module to generate random 
      10 digits number i.e numbers between 1000000000 and 9999999999 and 
      them all in list and finally choice 2 lucky numbers from that list.


 """
import random
tickets = []
for x in range(100):
    tickets.append(random.randrange(1000000000, 9999999999))
lucky = random.sample(tickets, 2)
print("list of all the tickets ", tickets)
print("Lucky 2 lottery tickets are", lucky)