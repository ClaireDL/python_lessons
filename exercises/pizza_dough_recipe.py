#!/usr/bin/env python

import sys


def proportion(*list_args):
    """
    Returns the proportions needed for the dough
    """
    percentage = float(list_args[2]) / 100
    flour = 8 * float(list_args[0]) / 9 * float(list_args[1])
    sourdough = (flour / 4)
    water = (percentage * flour - .5 * sourdough)
    return [flour, sourdough, water]


# prompts the user for the number of people
# if no entry is given, the default value is 1.
people = input("How many people? Default is 1. ")
if not people:
        people = 1.0

# prompts the user for the quantity of dough per person
# if no entry is given, the default value is 150g.
quantity = input("How much dough per person? 150g is the default amount. ")
if not quantity:
        quantity = 150.0

# prompts the user for the humidity percentage
# if no entry is given, the default value is 52%.
humidity = input("What humidity percentage? 52 is the default value. ")
if not humidity:
    humidity = 0.52

final_recipe = proportion(people, quantity, humidity)

# prints the recipe
if int(people) == 1:
    print("For {0:.0f} person, you need:".format(people))
else:
    print("For {0:.0f} people, you need:".format(people))
print("{0:.0f}g of flour, {1:.0f}g of sourdough, and {2:.0f}ml of water."
    .format(final_recipe[0], final_recipe[1], final_recipe[2]))
