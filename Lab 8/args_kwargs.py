# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:45:09 2024

@author: Rishita Agarwal
220150016

"""

#*args for list 
def sum_numbers(*args): #*args:arbitrary positional arguments 
    total=0
    for num in args:
        total+=num
    return total

result=sum_numbers(1,2,3,4,5)
print(result)

#** for pairs  ; **kwargs : arbitrary keyword arguments
def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
        
display_info(name="Teena", curr_name="March", city="Guwahati")
    
    

