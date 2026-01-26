### 1. Exploring two pointer Approach to solve DSA problem

####  How to think , is here two pointer approach is needed.

1. Problems belongs from either Array or LinkedList.

2. If data is sorted or needed to sort.

3. Merge or Remove Duplicate or Rearrange Data.

4. LL Questions (Detect Cycle).

5. When you have to find multiple stuffs (pair, triplets, Quadruple).

6. If we have restriction of not using extra space.

7. If you are using two pointer than you have to change at least one pointer or both after each operation.

8. When our both pointer meet at specific pointer or overlap each other than terminate the program.

> ####  Note 1. Two pointer and sliding window both are diff approaches.

> #### Note 2. Two pointer approach time complexity is O(n).

#### Little bit Dict practice in python
```py
print("Dictionary Exploration ")

# 1. how to create dict

myData = {
    "name":"Govind",
    "age":21,
    "email":"ergovindthakur@gmail.com",
    "extra":"abc"
}

print(myData)

# 2 accessing dict elem
print("My Age ",myData.get("age"))

# 3. add new data in dict
myData["working_Days"] = ["Mon","Tues","Wed"]
print(myData)

# 4. updating existing data in dict
myData["age"] = 20
print("My Age -> ",myData.get("age"))


# 5. removind dict item
# myData.pop("extra")
del myData["extra"]
# myData.clear() // It will clear all records
print(myData)

# 6. Looping through the dict
print(" ***************** Looped data ***************** ")
for data in myData:
    print(data, myData[data])

print(" ***************** Looped data 2 ***************** ")

for key , value in myData.items():
    print(key, value)
    
print()

# Dictionary methods interview favorites
print("Dictionary methods interview favorites")
print(myData.keys()) # it will return list of keys
print(myData.values()) # it will return list of values
print(myData.items()) # it will return list of tuples containing keys and value
myData.update({"age":"20.7"})
print(myData)
```