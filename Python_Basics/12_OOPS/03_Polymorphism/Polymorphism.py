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