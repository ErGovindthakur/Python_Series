name = 'Ajay'
print(name)
print(type(name))
print(name[0],name[-1])
# name[0] = 'V' string is not mutable

names = ["Ajay","Vijay"]

for elem in names:
     elem = elem.lower()
     for char in elem:
          # print(char)
          if char == "a" :
               print(char)
     print("Char")
