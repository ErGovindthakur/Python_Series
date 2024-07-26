# Exploring all about dictionary here
# Note-: Dictionary is a collection of keys-value pairs

myData = {
     "index":1,
     "name":"Govind",
     "marks":"100",
     "list":[1,2,3,4,5],
     # "name":"Working" Here name will be replace with name-Govind
}
print(myData)
print(myData["index"]) #Output -: it will print only index value
print(myData["list"]) # Output -: it will print only list values

# Properties of dictionary in python
'''
1) It is unordered,
2) It is mutable,
3) It is indexed,
4) Can not contain duplicate keys
'''

# Let's explore some method about dictionary in py

myDictionary = {
     "name":"Govind",
     "from":"India",
     "friend":"Me",
     "marks":[100,95,99,92,93]
}
print(myDictionary.items()) # return list of keys,values tuple
print(myDictionary.keys()) # will return list of containing dictionary keys
print(myDictionary.update({"friend":"mySelf"})) # It is used for props updating
print(myDictionary)
print(myDictionary.get("name"))


