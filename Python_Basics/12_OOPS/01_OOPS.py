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


class InvalidDetails(Exception):
    pass
    
class myDetails:
    def __init__(self,name,email,mob):
        self.__name = name
        self.__email = email
        self.__mob = mob
        
    def setDetails(self, name, email, mob):
        if isinstance(name,str) and name.strip():
            self.__name = name
        else:
            raise InvalidDetails("Name must be a valid string")
            
        if isinstance(email,str) and email.strip():
            self.__email = email
        else:
            raise InvalidDetails("Email must be a valid string")
            
        if isinstance(mob,int):
            self.__mob = mob
        else:
            raise InvalidDetails("Mob no must be a valid number")
            
    def getDetails(self):
        return (self.__name,
            self.__email,
            self.__mob)


md = myDetails("Govind","govind@gmail.com",123)
actualMd = md.getDetails();
print(f"md -. {actualMd}")


md2 = myDetails("Govind","govind@gmail.com",123)
actualMd2 = md2.setDetails("Govinda","govinda@gmail.com",12345)
print(f"md2 -> {md2.getDetails()}")
