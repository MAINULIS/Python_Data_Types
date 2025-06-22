"""
# A binary data type in Python is a way to represent data as a series of binary digits. which are 0s and 1s.
# This type of data is commonly used when dealing with things like files, images, or anything that can be represented using just two possible values.
# binary data types are bytes, bytearray and memory view
"""
## 1. Bytes
# Byte is an integer value between 0 and 255. it is immutable(we cannot modify)
# We can create bytes in Python using built-in "bytes()" function or by prefixing a sequence of numbers with "b".
b1 = bytes([3, 55, 78]) # Using bytes() function to create bytes
print(b1)

# Using prefix 'b' to create bytes
b2= b'hello'
print(b2)

# 2. Bytearray
# we use bytearray() function to declare a bytearray. it is mutable(we can modify).
b_a = bytearray([34, 43, 0])
print(b_a)

# by encoding a string. using "UTF-8" encoding −
b_a2 = bytearray("hellow", "utf-8")

# 3. memoryview
b_a3 = bytearray("hellow", "utf-8")
view = memoryview(b_a3)
print(view)

