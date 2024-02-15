# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:05:43 2024

@author: hp
"""
'''Rishita Agarwal 220150016
Created on 29-01-24 
Python Lab 2 - code along (list)'''

names=["First Name 1","Second Name 2","Third Name 3","Fourth Name 4"]

print(names)

#print("The length of string define in the above code is: "+len(names)) gives error as we cant concatenating an integer with the string directly
length_names=len(names)
length_names_str=str(length_names) #converting the integer to the string
print("The length of the list defined above is: "+length_names_str)

print("The length of list defined in the above code is: ",len(names))

#accessing the elements in the list-> 0 based indexing
print("=====================================")
print("Accessing the elements in the list")

print(names[0])
print(names[3])
print(names[-1])
print(names[-2])
print(names[2])


#another way of accessing
print(names[-1].title())

temp=names[0]
temp_last=names[-1]
print(f"The first element is {temp}. "+
      f"The last element is {temp_last}.")

#modfying element
names[1]='Modified Name'
print(names)

#adding elements at the end of the list
names.append("Fifth Name 5")
print(names)

#adding elements at some specific location
names.insert(1,'Adding 1st name')
print(names)
print(len(names))

#deleting
del names[1]
print(names)
print(len(names))

#fetching a value and delete it as well
temp_name_del=names.pop() #last value by default
print(temp_name_del)
print(names)

#deleting any specific value from the names list
temp_specific_del=names.pop(1)
print(temp_specific_del)
print(names)


#various operations we can do on the list using a for loop 
i=0
for name in names:
    print(i)
    print(name)
    i=i+1

print("The code is now completed...")
print("=============================")
#list of numerical values
roll_digits=[0,1,2,3,4,5,6,7,8,9]
roll_digits_func=list(range(0,10)) #range function excludes the last digit
print(roll_digits_func)

print("=============================")
print("Print the range of numbers")
for value in range(0,10):
    print(value)

print("=============================")
print("Print the slice of the list")
for value in roll_digits_func[3:6]:
    print(value)
 
print("=============================")
print("Print the first 6 numbers")
for value in roll_digits_func[:6]:
    print(value)

print("=============================")
print("Print the slice [6:]")
for value in roll_digits_func[6:]:
    print(value)
    
    
''' Dated feb 5, 2024 lab 3'''
print("============================== LAB 3 ===============================")
data=list(range(1,101))
data_int=list(range(1,101,2))
for value in range(1,101):
    #Printing all the numbers from 1 to 100 (both included)
    #print(value)
    print(f"The value = {value}.")
    #print(f"The value = "+str(value))
    
for value in range(1,101,3):
    #printing the values at an interval/steps of 3
    square=value**2
    #print(square)
    print(f"The square of value = {value} is {square}.")
    
#making a list of storing the squares of the values
print("========================= LISTS =================================")
squares=[]
for value in range(1,101,3):
    #square=value**2
    #print(square) --> it uses the value of square last value which was updated in the previous for loop
    #here the variables scope is not confined to a loop , it can be carried forward in other loops as well 
    #functions whereas has local scope for the variables
    #print({square})
    print(f"The sqaure of value = {value} is {value**2}.")
    squares.append(value**2)
    
#list comprehensions
print("===================== LIST COMPREHENSIONS ===================================")
squares=[value**2 for value in range(1,101,3)]

#you should always have a copy of your original data, do not completely apply all th emodifications on the original data itself

#tuple
print("============================= TUPLES ===========================")
data=(100,150,130)
print(f"The tuple printing data is: {data[0]}")









