#!/usr/bin/env python3
"""
Created on Thu Apr 16 12:22:03 2020

@author: Ashish Patel
"""
"""
Write a python program to plot a histogram, bar chart, line graph, scatter graph for some sample data.
Note: You can select any sample data to plot these graphs.

"""
import pandas as pd 
import matplotlib.pyplot as plt 

data = [['E001', 'M', 34, 123, 'Normal', 350], 
        ['E002', 'F', 40, 114, 'Overweight', 450], 
        ['E003', 'F', 37, 135, 'Obesity', 169], 
        ['E004', 'M', 30, 139, 'Underweight', 189], 
        ['E005', 'F', 44, 117, 'Underweight', 183], 
        ['E006', 'M', 36, 121, 'Normal', 80], 
        ['E007', 'M', 32, 133, 'Obesity', 166], 
        ['E008', 'F', 26, 140, 'Normal', 120], 
        ['E009', 'M', 32, 133, 'Normal', 75], 
        ['E010', 'M', 36, 133, 'Underweight', 40] ] 
  
dframe = pd.DataFrame(data, columns = ['EMPID', 'Gender','Age', 'Sales','BMI', 'Income'] )

#histogram
dframe.hist()  
plt.show()

#bar chart
dframe.plot.bar() 
plt.bar(dframe['Age'], dframe['Sales']) 
plt.xlabel("Age") 
plt.ylabel("Sales") 
plt.show() 


#line graph

plt.plot(dframe['Age'],dframe['Sales']) 
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.title('Age vs Sales ')  
plt.show() 


# scatter plot:

plt.scatter(dframe['Income'], dframe['Age']) 
plt.show() 
  
plt.scatter(dframe['Income'], dframe['Sales']) 
plt.show() 
  
plt.scatter(dframe['Sales'], dframe['Age']) 
plt.show() 