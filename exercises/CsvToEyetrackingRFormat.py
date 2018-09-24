#!/usr/bin/env python

import csv

# Step1
# Reads the data from the original file and prepares them for processing
# 1.1 Reads line by line
# 1.2 Extracts the 3 fields to be later processed
# 1.3 Stores the fields/lines in memory

original = "test.csv"

# Opens the original csv file to transform
with open(original, "rb") as csv_file:
    data = csv.reader(csv_file, delimiter = ",")

    # Checks if original file is empty
    if data == "":
        print("Error: empty file")

    # Phase 1.1: Reads line by line
    line_count = 0
    for row in data:
        if line_count == 0:
            header = ','.join(row)
            print ("Header is: %s" % header)
            line_count += 1
        else:
            print(','.join(row))
            line_count += 1
    # Phase 1.2: Field extraction
    fieldnames =
