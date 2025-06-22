## 5. Python Dictionary Data Type
# Python dictionaries type  kind of hash table type.
# The pairs of dictionary are separated by comma and put inside curly brackets {}. To establish mapping between key and value, the semicolon':' symbol is put between the two.
# In Python, dictionary is an object of the built-in dict class.Dictionary is a mutable object,
dicti  = {"brand": "samsung", "price": 43, "color" : "mad"}
print(type(dicti), dict)
print(dicti.keys())
print(dicti.values())

## 6. Python set data type
# Set is a Python implementation of set as defined in Mathematics.
set_data = {2023, "python", 33, (3+3j)}
print(type(set_data))
set2 = {'Java', 'Python', 'JavaScript'}
for elements in set2:
    print(elements)

set2.add("Go")
set2.remove("Java")
print(set2)


# 7. Boolean Data type
# Python Boolean data type is one of built-in data types which represents one of the two values either true or false
mai = False
print(type(mai))

# print false as a is not equal b.
a= 4
b= 3
print(bool(a==b))
# Returns False as X is None
x=None
print(bool(x))
# print false as a empty value
y=()
print(bool(y))

# 8. None type
# Python's none type is represented by the "nonetype."
no= None
print("no = ", no)
print("type of no = ",type(no))

