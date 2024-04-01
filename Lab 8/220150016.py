# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:59:59 2024

@author: Rishita Agarwal
220150016
Graded lab 8

"""

#task 1

name=input("Enter your name: ")
age=input("Enter your age (in years): ")


def get_valid_age(name,age):
    if age.isdigit() and int(age)>0:
        return True
    elif age.isalpha():
        print("The age is string.")
        return False
    elif age.isdigit() and int(age)<=0:
        print("The age is non positive integer.")
    elif age.isalnum():
        print("The age is alphanumeric.")
    elif age[0] == '-':
        print("The age is negative integer.")
    else:
        return False
    
while True:
    if get_valid_age(name,age):
        print(f"The name is {name} and the age is {age}.")
        break
    else:
        age=input("Enter a valid age: ")
        
            
   #example scenarios
     
  #Enter your name: 5.6
  #Enter your age (in years): 5.6
  #Enter a valid age: -4
  #Enter a valid age: 4.56
  #Enter a valid age: ert5
  #Enter a valid age: 56yh
  #Enter a valid age: tyhd
  #Enter a valid age: 5.6uhm
  #Enter a valid age: -5.h6
  #Enter a valid age: -5.6
  #Enter a valid age: 0
  #Enter a valid age: 4
  
  #The name is 5.6 and the age is 4.  

  
#task 2
name=input("Enter your name: ")
email=input("Enter your email address: ")

def get_valid_email(name,email):
    if "@" not in email or "." not in email:
        return False
    else:
        return True 
    

while True:
    if get_valid_email(name,email):
        print("Email is valid")
        print(f"The name of the person is {name} and the email address is {email}.")
        break
    else:
        email=input("Email is invalid. Please enter a valid email address: ")
    
#task 3

def get_square(num):
    num = float(num)
    print("Hello!\nThe square of", num, "is", num**2)


num = input("Enter a number: ")
def get_valid_number(num):
    while True:
        if num.isalpha() or num.isalnum():
            print("Invalid input! Please enter a valid number.")
            num=input("Enter a valid number: ")
            
        else:
            print("Yes a valid number.")
            get_square(num)
            break
           

get_valid_number(num)
    

#task 4

def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

def calculate_approx_e_x(x,num_terms):
    e_x = 0
    for i in range(num_terms):
        e_x += x**i / calculate_factorial(i)
    return e_x

def calculate_absolute_error(approx_value,actual_value):
    return abs(approx_value - actual_value)

import math

def main():

    while True:
            try:
                x = float(input("Enter the value of x: "))
                num_terms = int(input("Enter the number of terms for the Taylor series expansion: "))
                if x < 0 or num_terms < 0:
                    print("Please enter non-negative values for x and the number of terms.")
                else:
                    approx_value = calculate_approx_e_x(x,num_terms)
                    actual_value = math.exp(x)
                    absolute_error = calculate_absolute_error(approx_value,actual_value)
                    print(f"Approximate value of e^{x} is {approx_value}")
                    print(f"Actual value of e^{x} is {actual_value}")
                    print(f"Absolute error between the approximate and actual values is {absolute_error}")
                    break
            except ValueError:
                print("Please enter a valid number for x and the number of terms.")

if __name__=='__main__':
    main()
    
#task 5

def calculate_factorial(n):
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

def main():
    while True:
        try:
            n = int(input("Enter a non-negative integer: "))
            if n < 0:
                print("Please enter a non-negative integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid non-negative integer.")

    result = calculate_factorial(n)
    print(f"The factorial of {n} is {result}")
    
if __name__=='__main__':
    main()

#task 6

def calculate_series_sum(n):
        sum = 0
        for i in range(1, n+1):
            sum += 1/i
        return sum

def main():
    while True:
        try:
            n = int(input("Enter a positive integer: "))
            if n > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid positive integer.")

    sum = calculate_series_sum(n)
    print("The sum of the series is:", sum)


if __name__=='__main__':
    main()
    
#task 7

import math
def calculate_square_root(number):
    guess = number
    while True:
        new_guess = 0.5 * (guess + number / guess)
        if abs(new_guess - guess) < 0.0001:
            return new_guess
        guess = new_guess

def validate_input(input_str):
    try:
        number = float(input_str) #since it says positive number and not integer
        if number <= 0:
            return False
        return True
    except ValueError:
        return False
    

def main():
    while True:
        input_str = input("Enter a positive number: ")
        if validate_input(input_str):
            number = float(input_str)
            result = calculate_square_root(number)
            print(f"The square root of {number} is {result}")
            break
        else:
            print("Please enter a valid positive number.")

if __name__=='__main__':
    main()
    
    
#task 8

def calculate_fibonacci(n):
    if n==1:
        return [0]
    sequence=[0,1]
    term=2
    while(term<n):
        x=len(sequence)
        sequence.append(sequence[x-1]+sequence[x-2])
        term+=1
    return sequence
        
#print(calculate_fibonacci(3))

def main():
    while True:     
        try:
            n=int(input("Enter a positive integer: "))
            if n>0:
                print(f"The fibonacci sequence : {calculate_fibonacci(n)}.")
                break
            else:
                print("Enter a positive integer, not non-positive.")
        except ValueError:
            print("Enter a valid positve integer.")
    
    
if __name__ == "__main__":
    main() 
        




        
    
    



