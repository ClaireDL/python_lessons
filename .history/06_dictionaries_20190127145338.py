#!/usr/bin/env python

# Just imports print_function from the package future
from __future__ import print_function
import json

my_dict = {
    'name': "Claire",
    'age': 37,
    "weight": "too much"
}

my_dict_2 = [
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

json_my_dict = json.dump(my_dict_2)
