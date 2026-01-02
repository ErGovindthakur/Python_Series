'''  
1.  Single Inheritance
 One Parent → One Child
 Real-world idea

A Developer IS an Employee
'''

class Employee:
     def work(self):
          print("Employee works")


class Developer(Employee):
     def code(self):
          print("Devs code")
          


# creating instance for class
dev = Developer()
dev.work() # work method inherited from child class
dev.code() # child class method (dev)