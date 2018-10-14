#!/usr/bin/env python

import sys


def proportion(x, y, z):
    """
    Returns the quantity of flour, sourdough and water needed given the wanted amount of dough and people
    """
    percentage = float(z) / 100
    flour = 8 * x / 9 * y
    sourdough = (flour / 4)
    water = (percentage * flour - .5 * sourdough)
    return [flour, sourdough, water]


people = input("How many people to you want the pizza dough for? ")
quantity = input("How much dough per person do you want? 150g is the usual amount. ")
humidity = input("How much humidity percentage do you require for your dough? 52 is typical. ")

final_recipe = proportion(quantity, people, humidity)
#print(final_recipe)
print("You need %ig of flour %ig of sourdough %iml of water." % (final_recipe[0], final_recipe[1], final_recipe[2]))
