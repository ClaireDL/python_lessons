#!/usr/bin/env python

import sys


def calculate_ingredient_quantity(*list_args):
    """
    Returns the proportions needed for the dough
    """
    hydration = float(list_args[2]) / 100
    flour = 8 * float(list_args[0]) / 9 * float(list_args[1])
    sourdough = (flour / 4)
    water = (hydration * flour - .5 * sourdough)
    return [flour, sourdough, water]


# prompts the user for the number of people
# if no entry is given, the default value is 1.
people = raw_input("How many people? Default is 1. ")
if not people:
    people = 1.0

# prompts the user for the quantity of dough per person
# if no entry is given, the default value is 150g.
quantity_per_person = raw_input("How much dough per person? 150g is the default amount. ")
if not quantity_per_person:
    quantity_per_person = 150.0

# prompts the user for the hydration percentage
# if no entry is given, the default value is 52%.
hydration = raw_input("What hydration percentage? 52 is the default value. ")
if not hydration:
    hydration = 52

recipe = calculate_ingredient_quantity(people, quantity_per_person, hydration)

# prints the recipe
if int(people) == 1:
    print("For {0:.0f} person, you need:".format(people))
else:
    print("For {0} people, you need:".format(people))
print("{0:.0f}g of flour, {1:.0f}g of sourdough, and {2:.0f}ml of water."
    .format(recipe[0], recipe[1], recipe[2]))
