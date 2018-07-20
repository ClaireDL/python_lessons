#!/usr/bin/env python

import math
import sys

def area_circle():
    """
    Calculates the area for a circle based on radius
    """
    if len(sys.argv) < 3:
        print("ERROR: missing arguments: provide the radius")
        sys.exit(1)
    radius = float(sys.argv[2])
    if radius <= 0:
        print("ERROR: radius is a positive value")
        sys.exit(1)
    return radius * math.pi

def area_square():
    """
    Calculates the area for a square based on side
    """
    if len(sys.argv) < 3:
        print("ERROR: missing arguments, provide side")
        sys.exit(1)
    side = float(sys.argv[2])
    if side <= 0:
        print("ERROR: side is a positive value")
        sys.exit(1)
    return side**2

def area_rectangle():
    """
    Calculates the area for rectangle, product of base and side
    """
    if len(sys.argv) < 4:
        print("ERROR: missing arguments, provide base and side")
        sys.exit(1)
    base = float(sys.argv[2])
    height = float(sys.argv[3])
    if base <= 0 or height <= 0:
        print("ERROR: base and height are positive values")
        sys.exit(1)
    return base * height

def area_triangle():
    """
    Calculates the area for triangle based on base and height
    """
    if len(sys.argv) < 4:
        print("ERROR: missing arguments, provide base and height")
        sys.exit(1)
    base = float(sys.argv[2])
    height = float(sys.argv[3])
    if base <= 0 or height <= 0:
        print("ERROR: base and height are positive values")
        sys.exit(1)
    return base * height / 2

def area_rhombus():
    """
    Calculates the area for rhombus, product of base and side
    """
    if len(sys.argv) < 4:
        print("ERROR: missing arguments, provide base and height")
        sys.exit(1)
    base = float(sys.argv[2])
    height = float(sys.argv[3])
    if base <= 0 or height <= 0:
        print("ERROR: base and height are positive values")
        sys.exit(1)
    return base * height

# For missing command line arguments, prints an error message and exits
if len(sys.argv) <= 1:
    print("ERROR: command line arguments missing")
    sys.exit(1)

# Reads the name of the shape and applies the corresponding area calculation
# function
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
    sys.exit(1)

print("The area of the %s is %f." % (name_shape, area))
