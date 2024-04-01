# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:15:01 2024

@author: Rishita Agarwal
220150016
Graded Lab 9 (DA213)

"""

class Dog:
    '''An example to create a dog class... '''
    def __init__(self,name,age):
        '''Initialize name and age attributes'''
        self.name=name
        self.age=age
    
    def sit(self):
        '''Make the dog sit '''
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        '''the dog rolled'''
        print(f"{self.name} rolled over.") 
        
#making an instance from the class
my_dog=Dog("Tommy",4)

#calling methods of the class through the instance created
print(my_dog.roll_over()) #none was showed after this statement cuz this function does not return anything
my_dog.sit()

#accessing attributes like name and age from an instance
print(f"The name is {my_dog.name}")


from car import Car

my_new_car=Car("audi","a4",2024)
print("imported name: ",my_new_car.get_descriptive_name())

from car import ElectricCar as EV
my_leaf=EV("nission","leaf",2024)
print(my_leaf.get_descriptive_name())

   


    



