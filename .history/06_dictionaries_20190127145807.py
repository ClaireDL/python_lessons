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

json_my_dict = json.dump(list_of_dicts)

# Accessing a key in the dictionary
print("Name" + my_dict["name"])

# Setting the value of a key
my_dict["name"] = "Fabrizio"
