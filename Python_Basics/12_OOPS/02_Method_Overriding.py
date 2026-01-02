class Employee:
    def work(self):
        print("Employee working")

class Developer(Employee):
    def work(self):
        print("Developer writing code")


d = Developer()
d.work()   # overridden method
