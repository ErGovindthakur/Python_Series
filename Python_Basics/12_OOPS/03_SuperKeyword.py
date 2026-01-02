class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def show(self):
        print(self.name, self.language)


d = Developer("Govind", "Python")
d.show()
