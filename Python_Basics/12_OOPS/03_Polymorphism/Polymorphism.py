# writing polymorphism with method overriding

class Shape:
     def area(self):
          pass


class Square(Shape):
     def area(self):
          print("Area -> side * side")


class Circle(Shape):
     def area(self):
          print("Area -> pi * r * r")
          


# creating instance

shapes = [Square(),Circle()]

for shape in shapes:
     shape.area()


# 2. Example using phone unlock methods

# python polymorphism using method overriding

class PhoneUnlock:
    def Unlock(self):
        print("Phone Unlocked by following methods.....")

class FaceUnlock(PhoneUnlock):
    def Unlock(self):
        super().Unlock()
        print("Phone Unlocked by face.....")
        
class PinUnlock(PhoneUnlock):
    def Unlock(self):
        print("Phone Unlocked by pin.....")
        
class FingerUnlock(PhoneUnlock):
    def Unlock(self):
        print("Phone Unlocked by finger print.....")
        
        
class PatternUnlock(PhoneUnlock):
    def Unlock(self):
        print("Phone Unlocked by pattern.....")
        
    
    
pnUnlck = [FingerUnlock(),PinUnlock(),FaceUnlock(),PatternUnlock()]


for unlck in pnUnlck:
    unlck.Unlock()
    
    
    
