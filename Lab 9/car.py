# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:18:38 2024

@author: Rishita Agarwal
220150016
Graded Lab 9 (DA213)

"""


class Car:
    '''An example to create a dog class... '''
    def __init__(self,make,model,year):
        '''Initialize attributes...'''
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    
    def get_descriptive_name(self):
        '''detailed neatly formatted name'''
        long_name= f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        ''' print the statement showing the car's mileage'''
        print(f"This car has {self.odometer_reading} miles on the odometer.")
    def update_odometer(self,mileage):
        ''' set the odometer reading to the given value. reject the change if it attempts to roll the odometer back'''
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage #writing self.attribute means it is updated for the whole class
        else:
            print("You can't roll back on odometer.")
            
    def increment_odometer(self,miles):
        '''add the given amount to the odometer reading'''
        self.odometer_reading+=miles
        
#child class #    
class ElectricCar(Car):
    '''models aspects of a car, specific to electric car'''
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        #constructor of the parent clas is called
        '''Initialize the attributes of the parent class then initialize attributes specific to an electric car'''
        self.temp=5      
        
my_leaf=ElectricCar("nission","leaf","year")
print(my_leaf.get_descriptive_name())
        
my_new_car=Car("audit","a4",2024)
print(my_new_car.get_descriptive_name())

#print(my_new_car.read_odometer())
my_new_car.read_odometer()
        
#setting a default value for an attribute

#modify some value
my_new_car.odometer_reading=25
my_new_car.read_odometer()
