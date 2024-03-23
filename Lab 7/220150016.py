# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:02:41 2024

@author: Rishita Agarwal
220150016
Python Graded Lab 7

"""

#Task 1
name=input("Enter your name: ")
age=float(input("Enter your age(in years): "))

#a)

while age<0 or age!=int(age):
    age=float(input("Enter a valid age: "))

print(f"{int(age)} years.")

#b)
#Example scenario

age="rish"
#check=(int(age),,"No")
print(type(age))


age.isnumeric()
age.isalpha()

while True:
    if(age.isalpha()):
        age=input("Enter a valid numeric age: ")
    elif( not age.isnumeric()):
        age=input("Enter a positive integer as age: ")
    else:
        print(f"The valid age is: {age} years")
        break
    
print(age)

#c)
print(f"The name of the user is: {name} and age of the user is {int(age)} years.")


#Task 2
name=input("Enter the name of the user: ")
email=input("Enter the email address of the user: ")

while '@' not in email or '.' not in email:
    email=input("Enter a valid email address: ")
    
print(f"The user's name is {name} and the user's email address is {email}.")

#Task 3

number=input("Enter a number: ")

#a) c) d)
while number.isalpha():
    number=input("Enter a valid number: ")
    if(number=="stop"):
        break

#b)
square=int(number)*int(number)
print(f"Hi! I am {number}\n. My square is: {square}.")

#d) 

#float is a valid number here
while not new_num.isalpha():
    new_num=input("Enter a valid number: ")
    if(new_num.isalpha()):
        print(f"It is a string type number {new_num}.")
    else:
        print("Yes valid")
        break
    
#Task 4

import math

def fact(z):
    factorial=1
    while z>=1:
        factorial*=z
        z-=1
        
    return factorial

#a)

def taylor(x,epochs):

    e=math.e
    sum=1
    y=1
    
    #c)
    while epochs>0:
        sum+=(math.pow(x,y)/fact(y))
        #print(sum)
        y+=1
        epochs-=1
        
    return [sum,math.pow(e,x)]

x=int(input("Enter a number: "))

#b)
epochs=int(input("Enter the number of terms you want in the taylor series expansion: "))
list=taylor(x,epochs)
#print(list[0],list[1])
print(f"The approximation of {list[0]} calculated above is: {list[1]}.")

    
#e)
absolute_diff=math.abs(list[0]-list[1])
print(f"The absolute error between the approximated value and the actual value is: {absolute_diff}.")

#f) 
#Examples to show the different cases
x=input("Enter a number: ")
#x="a"
while True:
     try:
         x=float(input("Enter the number: "))
         break
     except ValueError:
         print("Please Enter a valid number.")
         continue
 
epochs=input("Enter the number of terms for the taylor series: ")
while True:
     if epochs.isnumeric():
         break
     else:
         epochs=input("Please enter a valid positve integer: ")
     
list1=taylor(x,epochs)
print(f"Actual: {list1[1]} and approximation: {list1[0]}.")


#g)
for i in range(0,10):
    while True:
        try:
            x=float(input("Enter the number: "))
            break
        except ValueError:
            print("Please Enter a valid number.")
            continue
    
    epochs=input("Enter the number of terms for the taylor series: ")
    while True:
        if epochs.isnumeric():
            break
        else:
            epochs=input("Please enter a valid positve integer: ")
        
    listt=taylor(x,epochs)
    print(f"Actual : {listt[1]} and Approximation : {listt[0]}. ")
    
        
#Task 5

#sine function : sin(x) = x+ x^3/3 + x^5/5 + ...

#a)
x=math.radians(input("Enter the value of x: "))
terms=int(input("Enter the valid number of terms to include in the expansion: "))

#b)
sum=0
for i in range(1,terms+1):
    y=2*i-1
    sum+=math.pow(x,y)
    
actual=math.sin(x)    
print(f"The approximate value of sin(x) is {sum} and the actual value is {actual}.")

#c)
abs_error=abs(sum-actual)
print(f"The absolute error between the approximated and the actual value is: {abs_error}.")


#Task 6
#a)

special=['!','@','#','$','%','^','&','*']
digits=['0','1','2','3','4','5','6','7','8','9']

flag=0
password=input("Enter a password: ")
while True:
    if(len(password)<8) or password==password.lower() or password==password.upper():
        password= input("Enter a valid password: ")
    else:
        for d in digits:
            for s in special:
                if d in password and s in password:
                    print("Valid password successfully recieved.")
                    flag=1
                    break
            if flag==1:
                break
    if flag==1:
        break
    else:
        password=input("Enter a valid password: ")  
           
                    
   
        

#Task 7
#a)
import random

num=random.randint(1,100)

#c)
test=0
while test<10:
    #b)
    guess=int(input("Guess the number generated: "))
    if guess==num:
        print(f"Congrats! You guessed the number {num} correctly in {test+1} guesses.")
        break
    #d)
    elif guess>num:
        print("Your guess is too high.")
        
    else:
        print("Your guess is too low.")
        
    test+=1


#Task 8
#a)
while True: 
    try:
        num=int(input("Enter a valid positive integer: "))
        if(num>0):
            break
        else: 
            print("Enter a valid value.")
            continue
    except ValueError:
        print("Enter a valid positive value.")
        continue
    
print(f"factorial of {num} is {fact(num)}.")


#Task 9
choice=(input("Enter 1 to convert celcius to fahrenheit and 2 to convert fahrenheit to celcius: ") )
while True:
    if choice.isnumeric() and (int(choice)==1 or int(choice)==2):
        break
    else:
        choice=input("Enter a valid choice. 1 or 2: ")
        
temp=float(input("Enter the value of temperature: "))

result=0
if int(choice)==1:
    result=(temp*9)/5 + 32
else:
    result=(temp-32)*5/9
    
print(result)


roots_classification = {}
keyword = "exit"
a = ''
b = ''
c = ''
while a!=keyword and b!=keyword and c!=keyword:
    try:
        a = input("Enter the value of a: ")
        if a == keyword:
            break
        a = float(a)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    try:
        b = input("Enter the value of b: ")
        if b == keyword:
            break
        b = float(b)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    c = input("Enter the value of c: ")
    if c == keyword:
        break
    if c.isnumeric():
        c = float(c)
    else:
        print("Invalid input. Please enter a valid number.")
        continue
    d = b**2-4*a*c
    if d > 0:
        roots_classification[(a, b, c)] = "Real and distinct"
    elif d == 0:
        roots_classification[(a, b, c)] = "Real and equal"
    else:
        roots_classification[(a, b, c)] = "Complex"

print("The roots classification is as follows:" )
for key, value in roots_classification.items():
    print(f"The roots of the equation {key[0]}x^2 + {key[1]}x + {key[2]} are {value}")
    
        
        
#task 11
bmi_classification = {}
keyword = "exit"
weight = ''
height = ''
while weight!=keyword and height!=keyword:
    weight = input("Enter your weight in kg: ")
    if weight == keyword:
        break
    try:
        weight = float(weight)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    if height == keyword:
        break
    try:
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    bmi = weight/(height**2)
    if bmi < 18.5:
        bmi_classification[bmi] = "Underweight"
    elif bmi < 24.9:
        bmi_classification[bmi] = "Normal weight"
    elif bmi < 29.9:
        bmi_classification[bmi] = "Overweight"
    else:
        bmi_classification[bmi] = "Obese"

    response = ''
    while response not in ['yes', 'no']:
        response = input("Do you want to continue? (yes/no): ")
        if response == 'yes':
            break
        elif response == 'no':
            weight = keyword
            height = keyword
            break
        else:
            print("Invalid input. Please enter a valid response.")
            response = input("Do you want to continue? (yes/no): ")
            continue

print("The BMI classification is as follows:" )
for key, value in bmi_classification.items():
    print(f"A person with BMI {key} is {value}")




    
    

        
       


