#!/usr/bin/env python3
"""
Created on Thu Apr 16 09:12:37 2020

@author: Ashish Patel
"""
"""
Write a NumPy program to compute the trigonometric sine, cosine and tangent array of angles given in degrees.

Example: Input Angles are 0, 30, 45, 60, 90.
         Output:
               sine: array of angles given in degrees
               [ 0. 0.5 0.70710678 0.8660254 1. ]
               cosine: array of angles given in degrees
               [ 1.00000000e+00 8.66025404e-01 7.07106781e-01 5.00000000e-01 6.12323400e-17]
               tangent: array of angles given in degrees
               [ 0.00000000e+00 5.77350269e-01 1.00000000e+00 1.73205081e+00 1.63312394e+16]

"""
import numpy
import math

arr = [0,30,45,60,90]

sine = numpy.sin(numpy.array(arr) * numpy.pi / 180.)
cos = numpy.cos(numpy.array(arr) * numpy.pi / 180.)
tan = numpy.tan(numpy.array(arr) * numpy.pi / 180.)

print("sine: array of angles given in degrees")
print(sine)

print("cosine: array of angles given in degrees")
print(cos)

print("tangent: array of angles given in degrees")
print(tan)