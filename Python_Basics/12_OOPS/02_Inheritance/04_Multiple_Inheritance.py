'''
4️. Multiple Inheritance
One Child → Multiple Parents
Real-world idea

A SmartPhone has features of Phone + Camera  
'''

# Note => Python allow multiple inheritance (unlike java)

class Phone:
     def call(self):
          print('Calling someone')

class Camera:
     def clickPhoto(self):
          print('Clicking a picture')

class SmartPhone(Phone,Camera): # Here SmartPhone class has two parent class
     def browse(self):
          print('Browsing webs')
          


# creating instances

sp = SmartPhone()

sp.call()
sp.clickPhoto()
sp.browse()