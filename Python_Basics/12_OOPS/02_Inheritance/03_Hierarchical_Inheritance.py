'''  
3️. Hierarchical Inheritance
One Parent → Multiple Children
Real-world idea

Vehicle → Car, Bike
'''

class Vehicle:
     def start(self):
          print("Vehicle started")

class Car(Vehicle):
     def drive(self):
          print("Drive the car")


class Bike(Vehicle):
     def ride(self):
          print("Have a bike ride")


# creating instance of classes

c = Car()
c.start()
c.drive()

b = Bike()
b.start()
b.ride()