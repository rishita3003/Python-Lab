# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 14:46:27 2024

Rishita Agarwal 220150016
12/02/2024 
3.00pm start time
Graded Lab 4

@author: hp
"""

#Q1
message=input("Enter a message: ")
#Hello World12{
answer=""
for x in message:
    if x==x.lower():
        answer=answer+x.upper()
    else:
        answer=answer+x.lower()
        
print(f"Altered Message: {answer}")

#Q2
str=input("Enter a string: ")
vowels=0
#converting whole string to lower case since we can ignore case sensitivity
str=str.lower()
for x in str:
    if x=='a':
        vowels+=1
    elif x=='e':
        vowels+=1
    elif x=='i':
        vowels+=1
    elif x=='o':
        vowels+=1
    elif x=='u':
        vowels+=1

print(f"Number of vowels in the input string are: {vowels}")

#Q3
#using slicing
str=input("Enter a string: ")
x=int(len(str))
#another way to slice is str[::-1]
print(f"Reversed string using slicing is: {str[-1:-x-1:-1]}")

'''using for loop
answer=""
for i in range(1,x):
    answer=answer+str[-i]
   # answer=str[i]+answer
    

print(f"Reversed string: {answer}")'''
    
#Q4
fav=('apple','cherry','grapes','watermelon')
   
#printing length of the tuple
x=int(len(fav)) 
print(f"Length of the tuple is: {x}")

#first and last element of the tuple
print(f"The first element of the tuple is: {fav[0]}.")
print(f"the last element of the tuple is {fav[x-1]}.")

#slicing the 2nd to 4th fruits, 4th is included in my code
print(fav[1:4])

#trying to change an element of tuple
fav[1]='mango'
print(fav)
'''gives error TypeError: 'tuple' object does not support item assignment'''
'''tuple is non modifiable thus no assignments or changes can be done in it '''
#Q5
#(a)
tup1=(1,2,3,4,5)
tup2=(6,7,8,9,10)

#direct concatenation 
tup3=tup1+tup2
print(tup3)

#(b)
print(f"Minimum value in tup1: {min(tup1)} and maximum value in tup1: {max(tup1)}.")
print(f"Minimum value in tup2: {min(tup2)} and maximum value in tup2: {max(tup2)}.")

#(c)
print(f"The sum of all elements of tup1 is: {sum(tup1)}.")
print(f"The sum of all elements of tup2 is: {sum(tup2)}.")
