#!/usr/bin/env python

# Just imports print_function from the package future
from __future__ import print_function
import json

my_dict = {
    'name': "Claire",
    'age': 37,
    "weight": "too much"
}

list_of_dicts = [
    {
        'name': "Claire",
        'age': 37,
        "weight": "too much"
    },
    {
        'name': "Fab",
        'age': 33,
        "weight": "too much"
    }
]

json_my_dict = json.dumps(list_of_dicts)
type(json_my_dict)

# Accessing a key in the dictionary
print("Name: " + my_dict["name"])

# Obtaining all the keys
print("All they keys: ", end="")
print(my_dict.keys())

# Obtaining all the values
print("All they values: ", end="")
print(my_dict.values())

# Checking if a key is present
print("Is \"birthday\" in my_dict? ", end="")
print("birthday" in my_dict)

# Accessing a key that doesn't exists with a default value
print("Birthday: " + my_dict.get("birthday", "Birthday not defined"))

# Updating a value of a dict in one line
# if "age" not in my_dict.keys():
#     my_dict["age"] = 0
# else:
#     my_dict["age"] = my_dict["age"] + 1
my_dict["age"] = my_dict.get("age", -1) + 1

# Setting the value of a key
my_dict["name"] = "Fabrizio"
print("New mame: " + my_dict["name"])

# Merging two dictionaries
print(my_dict)
my_dict_additional_info = {
    "age": 33,
    "birthday": "16/10/1985",
    "city": "Cattolica"
}
my_dict.update(my_dict_additional_info)
print(my_dict)

# Trying again the value that didn't exists before
print("Birthday: " + my_dict.get("birthday", "Birthday not defined"))

# Iterate through keys and values:
print("Content of my_dict")
for key, value in my_dict.iteritems():
    print("Key: %s, Value: %s" % (key, value))


# Functions with variable arguments
def greet_user(*user_list):
    for user in user_list:
        print("Hello %s" % user)
# Multiple arguments are stored in a single list
greet_user("Fabrizio", "Claire")
# Refresh on named parameters
greet_user(user_list=["Fabrizio", "Claire"])

# With double ** user_info becomes a dictionary
def greet_user_2(**user_info):
    for key, value in user_info.iteritems():
        print("%s: %s" % (key, value))

greet_user_2(name="Fabrizio", surname="Colonna")

# String templating
old_string_interpolation = "String: %s, Integer: %d" % ("string", 5)
positional_template = "String: {0}, Integer: {1}, Again the String: {0} {2}".format(
    "string", 5, "hello"
)
named_template = "Name: {name}, Surname: {surname}".format(
    name="Fabrizio",
    surname="Colonna"
)

# A simple implementation of the .format() function with variable arguments
def custom_format(my_string, *pos_elements, **named_elements):

    for i in range(len(pos_elements)):
        placeholder = "#" + str(i)
        my_string = my_string.replace(placeholder, pos_elements[i])

    for key, value in named_elements.iteritems():
        placeholder = "#" + key
        my_string = my_string.replace(placeholder, value)

    return my_string


# I can pass directly a dictionary to a varargs function
the_data = {
    'name': "Claire",
    'surname': "Delle Luche",
    'age': 37,
    "weight": "too much"
}
how_to_display_data = "Name: {name} {surname}, Age: {age}"

print(how_to_display_data.format(
    name=my_dict["name"],
    surname=my_dict["surname"],
    age=my_dict["age"],
))

print(how_to_display_data.format(**my_dict))
