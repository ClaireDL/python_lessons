#!/usr/bin/env python

# How to raise an exception
#raise Exception("Sample exception, you'll see this as description of the exception")

print("")

# Raising an exception of a different value
#raise ValueError("You can only choose between 1, 2 and 3")

print("")

# How to catch an exception
try:
    print("The code here is potentially unsafe and can raise/throw an exception")
    # Raise ValueError
    raise ValueError("You can only choose between 1, 2 and 3")
    print("All good, carry on")
# ValueError exception is managed here
except ValueError:
    print("Hi there! A ValueError exception has occurred, but we carry on")

print("")

# # We catch only the exception we specify
# try:
#     print("The code here is potentially unsafe and can raise/throw an exception")
#     # Here we raise ValueError
#     raise ValueError("You can only choose between 1, 2 and 3")
#     print("All good, carry on")
# # But this try/except block manages only IOError
# except IOError:
#     print("Nice management of IOError")

print("")

# How to catch multiple exception
try:
    print("The code here is potentially unsafe and can raise/throw an exception")
    # Raise ValueError
    raise IOError("Can't open file")
    print("All good, carry on")
# The block can manage ValueError but in this example we're not raising it
except ValueError:
    print("Hi there! A ValueError exception has occurred, but we carry on")
# IOError exception is managed here
except IOError:
    print("Nice management of IOError")

print("")

# You can manage all possible exception but never do it!!
try:
    print("The code here is potentially unsafe and can raise/throw an exception")
    raise SyntaxError("Can't open file")
    print("All good, carry on")
except Exception:
    print("Ignoring (handling nicely) all possible exception. VERY BAAADDDD")

print("")

# NEVER EVER EVER USE EXCEPTION TO 1) MANAGE THE NORMAL EXECUTION OF THE PROGRAM
# AND 2) NEVER EVER USE ROOT EXCEPTIONS
my_choice = None
try:
    my_choice = raw_input("Input a choice of 1, 2 or 3")
    # I'm "clever" and I use exception to manage the default value
    if my_choice not in [1, 2, 3]: raise ValueError
    # After that, something else raises a ValueError and the code becomes wrong
    raise ValueError("Can't open file")
except ValueError:
    # Set default value to 1... or fail???
    my_choice = 1

print("")

try:
    print("The code here is potentially unsafe and can raise/throw an exception")
    raise ValueError("This is the description of the except")
    print("All good, carry on")
# We save the exception in a variable and we make use of its information
except ValueError as my_value_error:
    import traceback
    print("Printing some information about the exception")
    print(my_value_error.message)
    print(traceback.format_exc())

print("")

# Good example of exceptions
try:
    import figlet
    __figlet_installed__ = True
except ImportError:
    __figlet_installed__ = False

# Later on...
if __figlet_installed__:
    print("I'm using figlet")
else:
    print("I'm not using figlet")
