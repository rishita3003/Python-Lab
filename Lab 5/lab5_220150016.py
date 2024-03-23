# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:08:38 2024

Rishita Agarwal
220150016
Lab 5

@author: hp
"""

import random 
import matplotlib.pyplot as plt

#rnd=3 can't give the name to the variable as that of the library name
#print(rnd)

listvalues=[1,2,3,4,5,6]
print(random.choice(listvalues)) #choice() is a function of random library

num_start=1
num_end=100
random_number=random.randint(num_start,num_end)
print(f"Random number is: {random_number}")
print(random.random())

random.seed(5)
print(random.random()) #0 inclusive and 1 exclusive

random.seed(700)
print(random.random())

random.seed(5)
print(random.random())

import numpy as np
import pandas as pd
import os

