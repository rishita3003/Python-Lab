# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 10:04:54 2024

@author: hp
Rishita Agarwal
220150016
Graded lab 6 (Make-Up)

"""
#task 1
print("Enter a list of integers: ")
length=7
list=[]

for i in range(0,length):
    x=int(input("Enter the element: "))
    list.append(x)
    
i=0    
for ele in list:
    if ele==15:
        list[i]=333
        break
    
    else:
        i+=1
        
    
print(f"The resultant list is: {list}.")

#task 2
str=input("Enter a string: ")
x=int(len(str))
idx=int(x/2)-1
if x%2==0:
    newstr=str[idx]+str[idx+1]
    print(f"The output string is {newstr}.")

else:
    newstr=str[idx]+str[idx+1]+str[idx+2]
    print(f"The output string is {newstr}.")
    
#task 3


array=[9,15,6,25,48,97,37,79,5,1,33]
x=len(array)
original=array

for j in range(0,x-1): 
    flag=0
    for i in range(0,x-1):
        if array[i]<array[i+1]:
            temp=array[i]
            array[i]=array[i+1]
            array[i+1]=temp
            flag=1
    
    if flag==0:
        break

print(f"The sorted array (descending) is: {array}.")

array=original

for j in range(0,x-1): 
    flag=0
    for i in range(0,x-1):
        if array[i]>array[i+1]:
            temp=array[i]
            array[i]=array[i+1]
            array[i+1]=temp
            flag=1
    
    if flag==0:
        break

print(f"The sorted array (ascending) is: {array}.")

#task 4

string="hEllo@Pranav2345&%3**^^%@IITG"
x=len(string)

digits=0
alphabets=0
special=0

for i in range(0,x):
    if string[i].isdigit():
        digits+=1
    elif string[i].isalpha():
        alphabets+=1
    else:
        special+=1
        
print(f"The number of digits, alphabets and special characters are {digits},{alphabets} and {special} respectively.")


#task 5
dict1={1:"hi",2:"bye",3:"a",4:"b"}
dict2={2:"b",1:"c",4:"aye",3:"c"}
dict3={2:"ab",5:"bye",4:"a",1:"hi"}
#dict2=dict3

flag=0

if len(dict1)!=len(dict2):
    flag=1

for i in dict1:
    if i not in dict2:
        flag=1
        break


if flag==1:
    print("FALSE")
else:
    print("TRUE")


#task 6

print("To convert from celcius to fahrenheit!")
f=float(input("Enter the temperature in fahrenheit: "))

c=(f-32)*5/9

print(f"The corresponding temperature in celcius for {f} degree fahrenheit is {c} degree celcius.")

c=float(input("Enter the temperature in celcius: "))
f=9*c/5 + 32
print(f"The corresponding temperature in fahrenheit for {c} degree celcius is {f} degree fahrenheit.")


#task 7
string = input("Enter a string: ")

reversed_string=string[::-1]
print(f"The reversed string using slicing is: {reversed_string}.")


#task 8

tup=(12, 'Poojitha', 22, 'Lab', 'Rishitha', 'IITG')

x=len(tup)

idx1=-1
idx2=-1
idx3=-1
for i in range(0,x):
    if tup[i]=='IITG':
        idx1=i
    elif tup[i]==23:
        idx2=i
    elif tup[i]=='Sushmitha':
        idx3=i
    
if idx1==-1:
    print("IITG is not present.")

else:
    print(f"The position  of IITG in the tuple is {idx1}.")

if idx2==-1:
    print("23 is not present.")
else:
    print(f"The position of 23 in the tuple is {idx2}.")
    
if idx3==-1:
    print("Sushmitha not found.")
else:
    print(f"The position of Sushmitha in the tuple is {idx3}.")



    
    




        
        
    
