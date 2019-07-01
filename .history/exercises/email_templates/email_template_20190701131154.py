#!/usr/bin/env python

import json
import csv
import fileinput



def find_pronoun(gender):
    if gender == "male":
        return ["him", "his"]
    elif gender == "female":
        return ["her", "her"]
    return ["them", "their"]


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


guest_info = "C:/Users/chdell/Dropbox/Fabrizio&Claire/python_lessons/exercises/email_templates/guest_list.json"
email_template = "C:/Users/chdell/Dropbox/Fabrizio&Claire/python_lessons/exercises/email_templates/email_template1.txt"

# this program creates a guest specific email by including in an email template the information
# contained in a dictionary that has one main entry per guest

# opens the guest list
with open(guest_info) as json_file:
    email = json.load(json_file)

    for entry in guest_info:
        # defines the title of the file
        print(entry)
        #title = "{0}_{1}.txt".format(entry["parent_last_name"], entry["parent_first_name"])

        # gets the birthday date in a Month Day format
        date = find_date(entry["date_of_birth"])

        # gets the correct form for pronouns and determiners
        pronouns = find_pronoun(entry["child_gender"])

        with fileinput.FileInput(email_template, inplace=True, backup='.bak') as file:
            for line in file:
                print(line.replace({parent_first_name}, entry["parent_first_name"]))
                print(line.replace({child_first_name}, entry["child_first_name"]))
                print(line.replace({date_of_birth}, date))
                print(line.replace({suggested_activity}, entry["suggested_activity"]))
                print(line.replace({him/her}, pronoun[0]))
                print(line.replace({his/her}, pronoun[1]))

        with open(title, "w+") as txt_file:
            # first line is email address
            txt_file.write(entry["email_address"])
            txt_file.write("\n")

            # write the main body of the email
            txt_file.write(email_template)
