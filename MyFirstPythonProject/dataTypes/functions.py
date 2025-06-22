"""
### Python functions
# A Python Function is a  block of organized, reusable code that is used to perform a single, related action.
"""
## Types of Function
## 1. Built -in functions
# Python's standard library includes number of built-in functions. Some of Python's built-in functions are print(), int(), len(), sum(), etc.

## 2. Functions defined in built-in modules

## 3. User defined functions(own function)
## without using function
cal_to_second = 24*60*60
#print(f"30 days are {30*cal_to_second} seconds")

# using function
name_of_unit = " hours" # global scope \ variable
calculation_to_minutes = 24*60


def days_to_units(num_of_days, comment):
    print(f"{num_of_days} days are {num_of_days * calculation_to_minutes} {name_of_unit}")
    print(comment)


days_to_units(30, "Awesome!")
days_to_units(2, "all good!")


## User Input (built-in function)
# input() is used to ask the user for an input and always returns a string
# Python stops executing when it comes to the input()

#user_input = input("Hey User, enter a number of days and I will convert it to hours! \n")
#print(user_input)

## return values
def day_to_second(num_of_days):
    if num_of_days > 0:
      return f"{num_of_days} days are {num_of_days * cal_to_second} second"
    elif num_of_days == 0:
        return "you entered a 0, please enter a valid positive number"


def validation_and_execute():
    if user_input.isdigit():
        user_input_num = int(user_input)
        calculated_value = day_to_second(user_input_num)
        print(calculated_value)
    else:
        print("your input is not a number. Don't ruin my program!")

user_input = input("Hey User, enter a number of days and I will convert it to hours! \n")
validation_and_execute()













