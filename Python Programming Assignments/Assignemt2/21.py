#!/usr/bin/env python3
"""
Created on Thu Apr 2 11:24:04 2020

@author: Ashish Patel
"""
"""
Using the module random and time in python generate a random date between given start and end
dates.
Example: Printing random date between 1/1/2016 and 3/23/2018
         Random Date = 02/25/2016

LOGIC:In this we take start and end date as input and defined a function 
      which we use random() and strptime() to generate a random date of the
      format %m/%d/%y which lies in the given interval of dates.

 """
import random
import time
def RandomDate(startDate, endDate ):
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'
    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))
    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate
startDate = str(input("Enter starting date (format : mm/dd/yyyy ) : "))
endDate = str(input("Enter ending date (format : mm/dd/yyyy ) :"))
print ("Random Date = ",RandomDate(startDate,endDate))