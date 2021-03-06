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
for key, value in my_dict.iteritems():
    print("Key: %s, Value: %s" % (key, value))
