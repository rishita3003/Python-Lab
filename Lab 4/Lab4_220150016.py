# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 14:14:56 2024

Rishita Agarwal
220150016
Lab 4 

@author: hp
"""

fruits=["Apple","Banana","Papaya","Mango","Pineapple"]
fruits=input("Enter the name of the fruit: ") #PAPAYA
 #replacing the list fruits by the string which we give as input
for name in fruits: #iterating in the string which we enter as input in fruits, thus each letter is read
    #print(name)
    if name=="Papaya":
        print(name.upper())
    elif name!="Kiwi":
        print("This fruit is not present in the fruit list.")
    else:
        print(name.title()) #first letter capital and rest in lower case
    
import os
source="C:\\Users\\hp\\OneDrive"

if os.path.exists(source)==True:
    print("The path exists.")
else:
    print("The path does not exist.")
    
if "PAPAYA" in fruits: #CHECKING IF THIS PARTICULAR STRING IS PRESENT IN FRUITS STRING OR NOT
    print("The fruit name is available")
    
print("KIWI" in fruits)

