#!/usr/bin/env python

import math
import sys

def area_circle():
    """
    Calculates the area for a circle based on radius
    """
    if len(sys.argv) < 3:
        print("ERROR: missing arguments: provide the radius")
        return False
    radius = float(sys.argv[2])
    if radius <= 0:
        print("ERROR: radius is a positive value")
        return False
    else:
        return radius * math.pi

def area_square():
    """
    Calculates the area for a square based on side
    """
    if len(sys.argv) < 3:
        print("ERROR: missing arguments, provide side")
        return False
    side = float(sys.argv[2])
    if side <= 0:
        print("ERROR: side is a positive value")
        return False
    else:
        return side**2

def area_rectangle():
    """
    Calculates the area for rectangle, product of base and side
    """
    if len(sys.argv) < 4:
        print("ERROR: missing arguments, provide base and side")
        return False
    base = float(sys.argv[2])
    height = float(sys.argv[3])
    if base <= 0 or height <= 0:
        print("ERROR: base and height are positive values")
        return False
    else:
        return base * height

def area_triangle():
    """
    Calculates the area for triangle based on base and height
    """
    if len(sys.argv) < 4:
        print("ERROR: missing arguments, provide base and height")
        return False
    base = float(sys.argv[2])
    height = float(sys.argv[3])
    if base <= 0 or height <= 0:
        print("ERROR: base and height are positive values")
        return False
    else:
        return base * height / 2

def area_rhombus():
    """
    Calculates the area for rhombus, product of base and side
    """
    if len(sys.argv) < 4:
        print("ERROR: missing arguments, provide base and height")
        return False
    base = float(sys.argv[2])
    height = float(sys.argv[3])
    if base <= 0 or height <= 0:
        print("ERROR: base and height are positive values")
        return False
    else:
        return base * height

# For missing command line arguments, prints an error message and exits
if len(sys.argv) <= 1:
    print("ERROR: command line arguments missing")
else:
    name_shape = str(sys.argv[1]).lower()
    if name_shape == "circle":
        area = area_circle()
    elif name_shape in ["rectangle", "rhombus"]:
        area = area_quadrilateral()
    elif name_shape == "triangle":
        area = area_triangle()
    elif name_shape == "square":
        area = area_square()
    else:
        print("ERROR: enter a valid shape name")
        area = False

    if area != False:
        print("The area of the %s is %f." % (name_shape, area))

print("Thank you for using this program.")