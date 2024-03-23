# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:16:52 2024

@author: Rishita Agarwal
220150016
18-3-24
Python Lab 7

"""
#while loop

number =  0
while number<=5:
    info=input("Tell me your experience(1-10) about this lab?\n")
    #it depends on the students
    #2
    print(f"The experience is as follows: {info}.")
    number=int(info)
    if (number<0):
        break
    else:
        print("The rating could be improved.")
    
    #if info>=1:  #data type is not same for comparison
    #    print("It is rated well.")
    #else:
    #    print("Not satisfactory.")
    
    if int(info)>=1:
        print("It is rated well.")
    else:
        print("Not satisfactory.")

x=1
while x<=10:
    x=x+1
    print(x)
    if x%2==0:
        continue
    print(x)
    

