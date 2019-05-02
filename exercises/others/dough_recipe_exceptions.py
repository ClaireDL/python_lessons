#!/usr/bin/env python

import sys

"""
Chosen names are really bad. What's x y z? What's percentage? What's final recipe? What's proportions?
All quantities are in grams
There's no typical HYDRATION
If a value is not provided it should be the default
Formatting of the output is important
Additional things to consider are oil and a blend of flours
"""

# user prompt to type in the number of people
# data validation: variable receives a default value
try:
    people = raw_input("How many people to you want the pizza dough for? 1 is the default ")
    if not people:
        people = 1.0
    else:
        isinstance(people, int) == True
        people = float(people)
except ValueError:
    print("Please enter the number of people as integers ")
    people = raw_input("How many people to you want the pizza dough for? 1 is the default ")
    people = float(people)

try:
    quantity = raw_input("How much dough per person do you want? 150g is the default amount. ")
    if not quantity:
        quantity = 150.0
    else:
        isinstance(quantity, float) == True
        quantity = float(quantity)
except ValueError:
    print("Please enter the quantity of dough in digits ")
    quantity = raw_input("How much dough per person do you want? 150g is the default amount. ")
    quantity = float(quantity)

try:
    hydration = raw_input("How much hydration percentage do you require for your dough? 52 is the default value. ")
    if not hydration:
        hydration = 0.52
    elif hydration not in range(0, 100):
        print("Please enter a hydration ratio between 0 and 100")
        hydration = raw_input("How much hydration percentage do you require for your dough? 52 is the default value. ")
    hydration = float(hydration)/100
except ValueError:
    print("Please enter hydration in digits")
    hydration = raw_input("How much hydration percentage do you require for your dough? 52 is the default value. ")
    hydration = float(hydration)/100

flour = 8 * people / 9 * quantity
sourdough = flour / 4
water = hydration * flour - .5 * sourdough

if int(people) == 1:
    print("For {0:.0f} person, you need:".format(people))
else:
    print("For {0:.0f} people, you need:".format(people))
print("{0:.0f}g of flour, {1:.0f}g of sourdough, and {2:.0f}ml of water.".format(flour, sourdough, water))
