#!/usr/bin/env python

# Types
my_string = "This is a string"
my_integer = 123
my_float = 123.45
my_boolean = False
my_list = ["a", 32, True, []]
my_dictionary = {
    "key_1": "string_1",
    "key_2": 123,
    "key_3": [1, 2, 3],
}
my_none = None

# Operators
print(123 + 321)
print("String1" + "String2")
print(False + False)
print(not (False or (True and True)))

# Conversion
print("This is number " + str(2))
print(int("123") + 321)
print(3 / 2)
print(float(3) / float(2))

# Assignment operators
a = 3
a = a + 2
print(a)
b = 3
b /= 2
print(b)

# If
if a + 2 >= 2:
    print("a + 2 is >= 2")
elif a - 3 >= 0:
    print("a + 2 is >= 0")
else:
    print("a + 2 is < 0")

# Same but less clean than above
if a + 2 >= 2:
    print("a + 2 is >= 2")
else:
    if a - 3 >= 0:
        print("a + 2 is >= 0")
    else:
        print("a + 2 is < 0")
