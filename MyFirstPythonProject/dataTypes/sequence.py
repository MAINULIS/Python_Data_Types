"""
## Python Sequence Data Type
#Sequence is a collection data type.It is an ordered collection of data type. It's positional index  start with 0.
# List, Tuple and Range are the sequence data types
"""
## List Data type
# Python List are the most versatile compound data type
# lists are mutable(can be reassign)
list_data = [2025,5, "python",4.44, 3+4j ]
list_data[1] = 55
print(list_data)
print(type(list_data))
print(list_data[3])
# a list object can also be an item in another list
list_obj= [[3,45, 2], ["shirt", "pant", "watch"]]
print(type(list_obj))

## List Operations
my_list = ["January", "February","March"]
my_list.append("April")
print(my_list)

## Tuple
# Python Tuple is another sequence data type similar with list
# tuples are enclosed within parentheses (...).cannot be updated (immutable).
tuple = (34, 32, 22, "python",( 4+4j))
print(tuple)
print(type(tuple))


## Range
# A Python range is an immutable sequence of numbers which is typically used to iterate through a specific number of items.
"""
# It is represented by the Range class.
#  range(start, stop, step)
start: Integer number to specify starting position, (Its optional, Default: 0)

stop: Integer number to specify ending position (It's mandatory)

step: Integer number to specify increment (gap), (Its optional, Default: 1)
"""
for i in range(1, 5, 2): # here, 1 represent start, 5 represent stop and 2 represent step
    print(i)

for i in range(7):
    print(i)

for i in range(202, 207, 2):
    print(i)


