# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:45:46 2024

Rishita Agarwal
220150016
Graded Lab 5

@author: hp
"""

#Q1
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))

if(y==0):
    print("Enter a valid number for checking divisibility.")
elif(x%y==0):
    print("YES, first number is divisible by second number.")
else:
    print("No, not divisible.")


#Q2
num=int(input("Enter the number: "))

if(num%2==0):
    print("It is an even number.")
else:
    print("It is an odd number.")
    
    
#Q3
a=float(input("first coefficient: "))
b=float(input("second coefficient: "))
c=float(input("third coefficient: "))

root_term=b*b-4*a*c

if(root_term==0):
    print("Real and equal roots.")
elif(root_term>0):
    print("Real and distinct roots.")
else:
    print("Complex roots.")

    
#Q4
wt=float(input("Enter the weight (in kg): "))
ht=float(input("Enter the height (in meters): "))

BMI=wt/(ht*ht)
print(f"The BMI is: {BMI}")

if(BMI<18.5):
    print("Underweight.")
elif(BMI<25):
    print("Normal Weight.")
elif(BMI<30):
    print("Overweight.")
else:
    print("Obesity.")
   
#Q5
import random
start=1
end=10
rand_num=random.randint(start,end)
print(f"Random number generated are: {rand_num}.")

attempts=5
flag=0
i=1
print(f"The number of attempts you have are: {attempts}.")
while(i<=attempts):
    print(f"Attempt {i}")
    guess=int(input("Enter your guess: "))
    if(guess<start or guess>end):
        print(f"Enter a number between {start} and {end}.")
        i=i-1
        
    elif(guess<rand_num):
        print("Too low! Try again.")
    elif(guess>rand_num):
        print("Too high! Try again.")
    else:
        flag=1
        print("Congratulations! You've guessed the number correctly.")
        break
    i=i+1
    
if(flag==1):
    print("Game ended successfully!")
else:
    print("Sorry, you've run out of attempts. The correct number was {guess}.")

