# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:01:12 2024

@author: Rishita Agarwal
220150016
Class Lab7
"""


import math

#trignometric functions
angle_degrees=45
angle_radians=math.radians(angle_degrees)
sin_value=math.sin(angle_radians)
cos_value=math.cos(angle_radians)
tan_value=math.tan(angle_radians)

#Logarithmic functions
log_value=math.log(100,10)
log10_value=math.log10(100)
log2_value=math.log2(100)

#print(log_value) #returns floating point
#print(log2_value) #returns floating point

#exponential and power functions
exp_value=math.exp(2)
pow_value=math.pow(2,10)
sqrt_value=math.sqrt(16)

#returns floating point
#print(pow_value)
#print(exp_value)
#print(sqrt_value)

#constants
pi_value=math.pi
e_value=math.e

print(sin_value,cos_value,tan_value)
print(log_value,log10_value,log2_value)
print(exp_value,pow_value,sqrt_value)
print(pi_value,e_value)