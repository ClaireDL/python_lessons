#!/usr/bin/env python
#
# Create a program to prepare emails for different users.
#
# You have to come up with the requirement knowing the final result.
# The purpose of the script you want to write is to send (for this script,
# just create the content) customized emails to a list of people.
# You want it to work not just for one email and just one list of people
# you want it to be generic.
#

import csv
import argparse


def load_template(template_file):
    """
    Loads a template from a file
    """
    with open(template_file, "r") as file:
        return file.read()


def parse_template(template, data):
    """
    Fills a template with the passed data
    """
    return template.format(**data)


def read_input(input_csv):
    """
    Reads the input CSV file and return a list of dictionaries
    """
    with open(input_csv, 'r') as file:
        return [dict(zip(["title", "first_name", "last_name"], row)) for row in csv.reader(file)]


def create_outputs(template, input_data, output_prefix):
    """
    Creates an output from the template file for each entry of the input list
    """
    for entry in input_data:
        print("Creating a file...")
        # Build the file name from the first and last name. As a choice, we want
        # all lower case and no spaces
        first_name = entry['first_name'].lower().replace(" ", "_")
        last_name = entry['last_name'].lower().replace(" ", "_")
        file_name = "{0}_{1}_{2}.txt".format(
            output_prefix, first_name, last_name
        )
        with open(file_name, "w") as file:
            file.write(parse_template(template, entry))


def main():
    # Read command line inputs and parameters
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'template_file',
        help='The path of the template.'
    )
    parser.add_argument(
        'input_csv',
        help='The CSV with the input list.'
    )
    parser.add_argument(
        'output_prefix',
        help='The prefix of the output files.'
    )
    args = parser.parse_args()

    #
    # Step #1: We load the template from file
    #
    template = load_template(args.template_file)

    #
    # Step #2: We load the input data from the CSV
    #
    input_data = read_input(args.input_csv)

    #
    # Step #3: We create the output files
    #
    create_outputs(template, input_data, args.output_prefix)

#
# Starting point
#
if __name__ == '__main__':
    main()
