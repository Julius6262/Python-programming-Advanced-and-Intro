# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__amount = 0
        self.__reading = 0

    def fill_up(self):
        self.__amount = 60
    
    def drive(self, km:int):
        
        if self.__amount < km:
            self.__reading += self.__amount
            self.__amount = 0

        else:
            self.__reading += km
            self.__amount -= km 
    
    def __str__(self):
        return f"Car: odometer reading {self.__reading} km, petrol remaining {self.__amount} litres"

