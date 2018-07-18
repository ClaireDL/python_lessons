#!/usr/bin/env python

# Two ways of defining strings
string1 = "sdfsdf"
print(string1)
string2 = 'sdfsdf'
print(string2)

# Triple double-quotes allows multi line strings (heredoc)
string3 = """line1
    line2
line3"""
print(string3)

# While without triple double-quotes:
string4 = "line1\n\tline2\nline3"
print(string4)

# To disable the usage of escape sequences
string5 = r"sgsg\nsadfsgf"
print(string5)

# Useful functions
test_string = "  AbCdEfGh  "
print(len(test_string))
print(test_string.lower())
print(test_string.upper())
print(test_string.rstrip())
print(test_string.lstrip())
print(test_string.strip())

# Strings are lists of characters
print(test_string[4])
print(test_string[3:6])
print(test_string[:6])
print(test_string[3:])
print(test_string[::-1])

# Composing
cleaned = test_string.lower().strip()
print(cleaned[::-1])

# Find and replace
print(test_string.find("bC"))
print(test_string.find("Nothing"))
print(test_string.replace("A", "Claire"))
print(test_string.replace(" ", "012"))
print(test_string.replace("Nothing", "975"))

# String interpolation
print("The price of %s is %f" % ("Pizza", 10.20))
# Old (bad) way
print("The price of " + "Pizza" + " is " + str(10.20))
print("My name is: %s" % "Fabrizio")
# New way of doing it
print("The price of {0} is {1:.2f}. I like {0}!".format("Pizza", 10.20))
