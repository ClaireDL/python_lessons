#!/usr/bin/env python

# Opens a file to do some operantions on it
example_file = open("my_example.txt", "w+")
example_file.write("This is a line in the file\n")
example_file.write("This is another line\n")
# Release the resources to the operating system
example_file.close()

# With performs the close operation for us and makes explicit the fact that we
# are working with an open file (or any equivalent structure that has a .close())
with open("my_example.txt", "a") as example_file:
    example_file.write("Line written inside with\n")

example_file = open("my_example.txt", "r")
# Reads the whole file as a single string
file_content = example_file.read()
print(file_content)
# A second read doesn't show anything because the pointer is at thend of the
# file
print(example_file.read())
# We move back at the beginning of the file
example_file.seek(0)
# And we can read (or perform other actions) again. We can move anywhere in the
# file
print(example_file.read())
example_file.close()

# I'm reading the file one line at the time and saving memory
with open("my_example.txt", "r") as example_file:
    for line in example_files.readline():
        print(line)
