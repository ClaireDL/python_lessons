#!/usr/bin/env python

import math
import sys


def formula_dispatcher():
    """
    Calls the function associated with each shape
    Returns an error message if name is invalid
    """
    name_shape = str(sys.argv[1]).lower()

    if name_shape == "circle":
        return area_circle()
    elif name_shape in ["rectangle", "rhombus"]:
        return area_quadrilateral()
    elif name_shape == "triangle":
        return area_triangle()
    elif name_shape == "square":
        return area_square()
    else:
        return False


def area_circle():
    """
    Calculates the area for a circle based on radius
    """

    if len(sys.argv) < 3:
        return "Error: missing argument, provide the radius"

    radius = float(sys.argv[2])

    if radius <= 0:
        return "Error: radius is positive"

    return radius * math.pi

def area_square():
    """
    Calculates the area for a square based on side
    """

    if len(sys.argv) < 3:
        return "Error: missing argument, provide the side"

    side = float(sys.argv[2])

    if side <= 0:
        return "Error: side is positive"

    return side ** 2

def area_rectangle():
    """
    Calculates the area for rectangle, product of base and side
    """

    if len(sys.argv) < 4:
        return "Error: missing argument, provide the two sides"

    base = float(sys.argv[2])
    height = float(sys.argv[3])

    if base <= 0 or height <= 0:
         return "Error: the sides are positive"

    return base * height

def area_triangle():
    """
    Calculates the area for triangle based on base and height
    """

    if len(sys.argv) < 4:
        return "Error: missing argument, provide the base and height"

    base = float(sys.argv[2])
    height = float(sys.argv[3])

    if base <= 0 or height <= 0:
        return "Error: base and height are positive"

    return base * height / 2

def area_rhombus():
    """
    Calculates the area for rhombus, product of base and side
    """

    if len(sys.argv) < 4:
        return "Error: missing argument, provide the diagonals"

    base = float(sys.argv[2])
    height = float(sys.argv[3])

    if base <= 0 or height <= 0:
        return "Error: the diagonals are positive"

    return base * height

# Checks validity of input and prints error message
if len(sys.argv) <= 1:
    print("ERROR: command line arguments missing")

elif formula_dispatcher() == False:
    print("ERROR: enter a valid shape name")

elif type(formula_dispatcher()) is str:
    print(formula_dispatcher())

# Prints the result of the relevant area calculator if input is valid
else:
    shape = str(sys.argv[1]).lower()
    print("The area of the %s is %f." % (shape, formula_dispatcher()))

# Thank you message for the user
print("Thank you for using this program.")
