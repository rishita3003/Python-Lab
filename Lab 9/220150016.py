# -*- coding: utf-8 -*-
"""
Created on Mon Apr 1 15:09:26 2024

@author: Rishita Agarwal
220150016
Graded Lab 9 (DA213)

"""

#task 1
class User:
    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email
        
    def get_valid_age(self): 
        name=input("Enter the name: ")
        age=input("Enter the age: ")
        
        while True:
            if age.isnumeric() and int(age)>0:
                break
            age=input("Enter a valid age: ")
        print("Got the valid age.")
         
    def get_valid_email(self):
        email=input("Enter your email address: ")
        while True:
            if "." in email and "@" in email:
                break
            email=input("Enter a valid email: ")
            
        print("Got the valid email.")
            
    def get_square(self,num):
        square=num*num
        print(f"The square of {num} is {square}.")
        
        
#a)
uu=User("",'',"")
uu.get_valid_age() #it runs and asks for input of age from user

#b)
uu.get_valid_email() #it runs and asks for the input of email from user


#c)
while True:
    num=input("Enter the number: ")
    try:
        uu.get_square(float(num))
    except ValueError:
        if num=="exit":
            print("Exiting the loop.")
            break

#d)
user1=User("Rish",'19',"blank@gmail.com")
user2=User("Kris",'24',"kk@gmail.com")
user3=User("Minnie",'15',"Min45@gmail.com")

#task 2
import math
e=math.e

class TaylorSeries:
    def calculate_factorial(self,n):
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return fact
    
    def calculate_approx_e_x(self,x,num_terms):
        approx=1
        for i in range(1,num_terms+1):
            approx+=math.pow(x,i)/self.calculate_factorial(i)
            
        return approx
        
    def calculate_absolute_error(self,approx_value,actual_value):
        return abs(actual_value-approx_value)
   


class UserInterface:
    def get_user_input():
        while True:
            try:
                x=float(input("Enter the value of x: "))
                num_terms=int(input("Enter the number of terms for approximation: "))
                if num_terms>0:
                    break
                else:
                    print("Enter positive integeral number of terms.")
                
            except ValueError:
                print("Enter a numeric value for x and positive integral value for the number of terms.")
        
        return x,num_terms
         
    def display_results(approx_value,actual_value,absolute_error):
        print(f"The approx value from taylor series is {approx_value}, the actual value is {actual_value} and the absolute error between these is {absolute_error}.")
        
            
'''x=5
num_terms=10        
t=TaylorSeries()
print(t.calculate_approx_e_x(x, num_terms))
print(math.pow(e,x))
t.calculate_absolute_error(t.calculate_approx_e_x(x,num_terms), math.pow(e,x))'''

t=TaylorSeries()
ui=UserInterface

x,num_terms=ui.get_user_input()

approx=t.calculate_approx_e_x(x,num_terms)
actual=math.pow(e,x)
error=t.calculate_absolute_error(approx, actual)

ui.display_results(approx, actual, error)

 
#task 3

class SquareRootCalculator:
    def calculate_square_root(number):
        #initial guess
        guess = number/2
        #loop until the guess is close enough
        while abs(guess*guess - number) > 0.0001:
            guess = (guess + number/guess)/2
            
        return guess
        
        
    @staticmethod 
    def validate_input(input_str):
        try:
            input_str=float(input_str)
            return True
        except ValueError:
            return False
        
sqc=SquareRootCalculator

class UserInterface:
    def get_user_input():
        while True:
            num=input("Enter a positive number: ")
            if sqc.validate_input(num)==True:
                return float(num)
            else:
                num=input("Please enter a valid positive number: ")
                
    def display_results(square_root):
        print(f"The calculated square root is {square_root}.")
        
        
uii=UserInterface
num=uii.get_user_input()
square_root=sqc.calculate_square_root(num)
uii.display_results(square_root)


#task 4
class FibonacciSequence:
    def calculate_fibonacci(n):
        siz=2
        if n==1:
            return [0]
        liss=[0,1]
        for i in range(1,n-1):
            liss.append(liss[siz-1]+liss[siz-2])
            siz+=1
        return liss

fs=FibonacciSequence

class UserInterface:
    def get_user_input():
        while True:
            try:
                n=int(input("Enter a positive integer: "))
                if n>0:
                    return n
                if n<=0:
                    print("Enter a positive integral n.")
            except ValueError:
                print("Enter a valid value of n.")
                
    def display_fibonacci_sequence(sequence):
        print("The fibonacci seqeunce is: ",sequence)
        
    
ui3=UserInterface
n=ui3.get_user_input()
sequence=fs.calculate_fibonacci(n)
ui3.display_fibonacci_sequence(sequence)

        
        
        
  
    

    


    
    
            
        
        
        



