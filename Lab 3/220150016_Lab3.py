# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:56:56 2024
Rishita Agarwal 220150016
Graded Lab 3

@author: hp
"""
#Q1
print("The first 55 numbers are as follows: ")
for num in range(1,56):
    print(num)

#Q2
#using list comprehension
numList=[value for value in range(1,1001)]
for i in range(0,1000):
    #accessing through indices
    print(numList[i])

#print(numList[0])
#print(numList[50])

#Q3
listNum=[value for value in range(1,1001)]
print(f"The minimum value in the list is: {min(listNum)}")
print(f"The maximum value in the list is: {max(listNum)}")
    
#Q4
print(f"The sum of the numbers in the above list is: {sum(listNum)}")
#(1000)*(1001)/2 = 500*1001= 500500 - verify

#Q5
#printing a sequence of odd numbers
odd=[]
for num in range(1,56,2):
    odd.append(num)

length=len(odd)
print("The list of odd numbers is as follows: ")
for i in range(0,length):
    #here due to 0 based indexing the last index would be length-1
    print(odd[i])

#Q6
#List of multiples of 3
print("The multiples of 3 are as follows: ")
mul_three=[value for value in range(3,301,3)]
length_three=len(mul_three)
for i in range(0,length_three):
    print(mul_three[i])

#Q7
print("The cubes of the first 100 numbers are: ")
cubes=[]
for i in range(1,101):
    cubes.append(i**3)
    
for i in range(0,100):
    print(cubes[i])
    
#Q8
print("Used list comprehension to make a list of cubes.")
cubes=[value**3 for value in range(1,101)]

#Q9
print("The list of even numbers is: ")
for num in range(2,56,2):
    print(num)

#Q10
print("The list of squares of first 20 numbers is as follows: ")
squares=[]
for i in range(1,21):
    squares.append(i**2)

for i in range(0,20):
    print(squares[i])