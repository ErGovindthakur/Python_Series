'''  
Multilevel Inheritance
Parent → Child → Grandchild 

Real-world idea
Person → Employee → Manager
'''

class Person:
     def identity(self):
          print("I am a person")

class Employee(Person):
     def job(self):
          print("I'm an Employee")


class Manager(Employee):
     def manage(self):
          print("I manage a team")


m = Manager()

m.identity()
m.job()
m.manage()