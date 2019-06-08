#!/usr/bin/env python

import json
import csv

def email(parent, child, date, direct_pronoun, game, possessive_pronoun):
    test = """
    Dear {0},

    A little bird told us that {1}'s birthday is coming up on {2}...
    We would like to invite {3} to a game of {4} along with {5} friends.
    Please let us know the party size you would like us to organise!

    We look forward to hearing from you!

    Best wishes,

    Party time
    """.format(parent, child, date, direct_pronoun, game, possessive_pronoun)

    return test

def find_pronoun(gender):
    if gender == "male":
        return ["him", "his"]
    else:
        return ["her", "her"]

def find_date(date):
    birthday = date.split("/")
    month_dict = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
    }
    return "{0} {1}".format(month_dict[birthday[1]], birthday[0])


# composes the invitation email and saves it as text file
file_path = "C:/Users/chdell/Dropbox/Fabrizio&Claire/python_lessons/exercises/chapter_based/ch06_guest_list.json"
with open(file_path) as json_file:
    data = json.load(json_file)
    for entry in data:
        # defines the title of the file
        title = "{0}_{1}.txt".format(entry["parent_last_name"], entry["parent_first_name"])

        # gets the birthday date in a Month Day format
        date = find_date(entry["date_of_birth"])

        with open(title, "w+") as txt_file:
            pronouns = find_pronoun(entry["child_gender"])
            # first line is email address
            txt_file.write(entry["email_address"])
            txt_file.write("\n")

            # write the main body of the email
            email_body = email(entry["parent_first_name"], \
                               entry["child_first_name"], \
                               date, \
                               pronouns[0], \
                               entry["suggested_activity"], \
                               pronouns[1] )
                               txt_file.write(email_body)
