# Practicing basic of oops syntax in python

class car:
     def __init__(self,brand,speed):
          self.brand = brand
          self.speed = speed
     
     
     def showCarDetails(self):
          print("Brand -> ",self.brand)
          print("Speed -> ",self.speed)
          


# creating instance of class (object)

c1 = car("BMW",120)
c1.showCarDetails()