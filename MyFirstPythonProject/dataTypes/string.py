# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:

## 1. Text type: String
Name = "Python"
print("My name is "+ Name)
#1.1 slicing string (index start with 0 with first character)
text = "Hello, World"
print(text[3: 9])
print(text[: 5]) # slice from beginning
print(text[2:]) # slice to the end
# 1.2 negative index (gets specific word or letters ) negative index work from end
print(text[-9: -2])

# Python - Modify Strings
# 1.3 upper case
print(text.upper())

# 1.4 lower case
print(text.lower())

# 1.5 remove whitespace (The strip() method removes any whitespace from the beginning or the end)
print(text.strip())

# 1.6  replace string
print(text.replace("H", "J"))

# 1.7 split string
print(text.split(" , "))

# 1.8 string concatenation
a1 = "hi"
a2 = "there!"
a3 = a1 +" " +a2
print(a3)

print("20 days are "+ str(50) +" minutes")
cal_to_second = 24*60*60
print(f"20 days are {20*24*60} minutes")
print(f"30 days are {30*cal_to_second} seconds")
print(f"5 days are {5*cal_to_second} seconds")

## 1.9 format string (f-string)
price = 34
txt= f"The phone price is {price:.2f}"
txt1= f"The phone price is {price}"
print(txt)
print(txt1)

## 2 Escape Character(An escape character is backslash "\")
txt3 = "We are the so-called \"Vikings\" from the north."
print(txt3)
# 2.1 backslash
text1 = " I will eat mango \\ banana"
print(text1)
# 2.2 new line
text2 ="hellow \nWorld"
print(text2)
