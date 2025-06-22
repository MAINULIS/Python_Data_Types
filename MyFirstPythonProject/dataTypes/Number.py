
## 2. Numeric Type : integer(int), float, complex
# 2.1 int
x= 73
y= 433
if x>y:
    print("ok")
else: print("bad")

# 2.2 floating number
x1 = 43.3
y2 = 33.4
print(x1 - y2)

# 2.3 complex
x3 = 4j
print(type(x3))

## 3 Type Conversion
x4 = 2
y4 = 2.5
z4 = 4j
print(type(z4))
# 3.1 convert from int to complex:
com = complex(x4)
print(com)
#float to int:
b = int(y4)
print(b)
