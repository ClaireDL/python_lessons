#!/usr/bin/env python

import math
import sys


def area_circle():
    """
    Prints the area for a circle based on radius
    """
    if len(sys.argv) < 3:
        print("ERROR: missing radius of the circle")
        sys.exit(1)

    radius = float(sys.argv[2])
    if radius <= 0:
        print("ERROR: radius must be a positive value")
        sys.exit(1)

    return radius * math.pi


def area_square():
    """
    Prints the area for a square based on side
    """
    if len(sys.argv) < 3:
        print("ERROR: missing side of the square")
        sys.exit(1)

    side = float(sys.argv[2])
    if side <= 0:
        print("ERROR: side must be a positive value")
        sys.exit(1)

    return side ** 2


def area_rectangle():
    """
    Prints the area for rhombus and rectangle, product of base and side
    """
    if len(sys.argv) < 4:
        print("ERROR: missing one or both sides of the rectangle")
        sys.exit(1)

    base = float(sys.argv[2])
    height = float(sys.argv[3])
    if base <= 0 or height <= 0:
        print("ERROR: base and height must be positive values")
        sys.exit(1)

    return base * height


def area_triangle():
    """
    Calculates the area for triangle based on base and height
    """
    if len(sys.argv) < 4:
        print("ERROR: missing base or height of the triangle")
        sys.exit(1)

    base = float(sys.argv[2])
    height = float(sys.argv[3])
    if base <= 0 or height <= 0:
        print("ERROR: base and height must be positive values")
        sys.exit(1)

    return base * height / 2


def area_rhombus():
    """
    Calculates the area for rhombus, product of base and side
    """
    if len(sys.argv) < 4:
        print("ERROR: missing one or both sides of the rhombus")
        sys.exit(1)

    base = float(sys.argv[2])
    height = float(sys.argv[3])
    if base <= 0 or height <= 0:
        print("ERROR: base and height must be positive values")

    return base * height


if len(sys.argv) <= 1:
    print("ERROR: you must specify the type of the shape")
    sys.exit(1)

shape_name = str(sys.argv[1]).lower()

if shape_name == "circle":
    area = area_circle()
elif shape_name in ["rectangle", "rhombus"]:
    area = area_quadrilateral()
elif shape_name == "triangle":
    area = area_triangle()
elif shape_name == "square":
    area = area_square()
else:
    print("ERROR: enter a valid shape name")
    sys.exit(1)

print("The area of %s is %f" % (shape_name, area))
