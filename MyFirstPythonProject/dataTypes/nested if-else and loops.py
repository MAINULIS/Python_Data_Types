from helper import validate_and_execute, user_input_message
## from helper import * (means import the whole module)
## import helper (means import the whole module but when we will use we should use helper.dash)


user_input =""
while user_input != "exit":
  user_input = input(user_input_message)
  days_and_unit = user_input.split(":")
  print(days_and_unit)
  days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
  print(days_and_unit_dictionary)
  validate_and_execute(days_and_unit_dictionary)
