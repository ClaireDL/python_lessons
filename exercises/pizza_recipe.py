#!/usr/bin/env python

import sys


def proportion(x, y):
    """
    Returns the quantity of flour, sourdough and water needed given the wanted amount of dough and people
    """
    flour = 8 * x / 9 * y
    sourdough = (flour / 4) * y
    water = (.52 * flour - .5 * sourdough) * y
    return [flour, sourdough, water]


people = input("How many people to you want the pizza dough for?")
quantity = input("How much dough per person do you want? 150g is the usual amount")

final_recipe = proportion(quantity, people)
#print(final_recipe)
print("You need %ig of flour %ig of sourdough %iml of water." % (final_recipe[0], final_recipe[1], final_recipe[2]))
