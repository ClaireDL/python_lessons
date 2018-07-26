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
        return "error_argument"

    radius = float(sys.argv[2])

    if radius <= 0:
        return "error_positive"

    return radius * math.pi


def area_square():
    """
    Calculates the area for a square based on side
    """

    if len(sys.argv) < 3:
        return "error_argument"

    side = float(sys.argv[2])

    if side <= 0:
        return "error_positive"

    return side ** 2


def area_rectangle():
    """
    Calculates the area for rectangle, product of base and side
    """

    if len(sys.argv) < 4:
        return "error_argument"

    base = float(sys.argv[2])
    height = float(sys.argv[3])

    if base <= 0 or height <= 0:
         return "error_positive"

    return base * height


def area_triangle():
    """
    Calculates the area for triangle based on base and height
    """

    if len(sys.argv) < 4:
        return "error_argument"

    base = float(sys.argv[2])
    height = float(sys.argv[3])

    if base <= 0 or height <= 0:
        return "error_positive"

    return base * height / 2


def area_rhombus():
    """
    Calculates the area for rhombus, product of base and side
    """

    if len(sys.argv) < 4:
        return "error_argument"

    base = float(sys.argv[2])
    height = float(sys.argv[3])

    if base <= 0 or height <= 0:
        return "error_positive"

    return base * height

def error_argument():
    """
    Gets name shape to provide the relevant measure names
    """
    name = str(sys.argv[1]).lower()
    if name == "circle":
        return "radius"

    elif name == "rectangle":
        return "length and width"

    elif name == "rhombus":
        return "diagonals"

    elif name == "triangle":
        return "base and height"

    elif name == "square":
        return "side"

    else:
        return False

# Checks validity of input and prints error message
if len(sys.argv) <= 1:
    print("ERROR: command line arguments missing")

elif formula_dispatcher() == False:
    print("ERROR: enter a valid shape name")

elif formula_dispatcher() == "error_positive":
    print("ERROR: %s is/are positive value(s)" % (error_argument()))

elif formula_dispatcher() == "error_argument":
    print("ERROR: missing arguments, provide %s" % (error_argument()))

# Prints the result of the relevant area calculator if input is valid
else:
    shape = str(sys.argv[1]).lower()
    print("The area of the %s is %f." % (shape, formula_dispatcher()))

# Something else that the program must do after whatever happened before
print("Thank you for using this program.")
