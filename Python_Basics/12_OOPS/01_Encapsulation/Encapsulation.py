# Writing two programs to understand basic of encapsulation working

class Student_Marks:
     def __init__(self,marks):
          self.__marks = marks
     
     
     def get_marks(self):
          return self.__marks
     
     def set_marks(self,new_marks):
          if new_marks > 0:
               self.__marks = new_marks
          else:
               print("Invalid marks")


# creating an instance to access above class

s1 = Student_Marks(90)
print(f"You got -> {s1.get_marks()} marks")

s1.set_marks(0)

s1.set_marks(99)
print(f"You got -> {s1.get_marks()} marks")