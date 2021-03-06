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
print("Name" + my_dict["name"])

# Setting the value of a key
my_dict["name"] = "Fabrizio"
print("Name" + my_dict["name"])

# Merging two dictionaries
print(my_dict)
my_dict_additional_info = {
    "age": 33,
    "birthday": "16/10/1985",
    "city": "Cattolica"
}
my_dict.update(my_dict_additional_info)
print(my_dict)
