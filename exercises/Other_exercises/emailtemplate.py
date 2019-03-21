#!/usr/bin/env python

volunteer_list = [
    {
        'parent_name': "Mrs Huntingdon",
        'child_name': "Peter",
        "email": "definitelymoded@gmail.com",
        "gender": "boy"
    },
    {
        'parent_name': "Mrs Cat",
        'child_name': "Tom",
        "email": "definitelymoded@gmail.com",
        "gender": "boy"
    }
]

for child in volunteer_list:
    for key in child:
        print("""{0}
        Dear {1},
        We would like to invite you and {2} to the Babylab for a study.
        """.format(child[email], child[parent_name], child[child_name]))
