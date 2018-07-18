#!/usr/bin/env python

import math
import sys

def argument_list():
    """
    Detailed expected arguments depending on the shape
    """
    if sys.argv[1] == "circle":
        print("Provide the radius for a circle")
    elif sys.argv[1] == "square":
        print("Provide the side of the square")
    elif sys.argv[1] == "rectangle":
        print("Provide the length and width")
    elif sys.argv[1] == "rhombus" or sys.argv[1] == "triangle":
        print("Provide the base and height")

def input_validation_1_measure():
    """
    Checks that the correct number of command line argument including a positive
    value are provided. Sends error messages if conditions are not met
    """
    if len(sys.argv) < 3:
        print("ERROR: missing arguments")
        argument_list()
        return False
    elif len(sys.argv) >= 4:
        print("ERROR: too many arguments")
        argument_list()
        return True
    else:
        var_1 = float(sys.argv[2])
        if var_1 <= 0:
            print("ERROR: enter a positive value")
            return False
        else:
            return True

def input_validation_2_measures():
    """
    Checks that the correct number of command line argument including positive
    values are provided. Sends error messages if conditions are not met
    """
    if len(sys.argv) < 4:
        print("ERROR: missing arguments")
        argument_list()
        return False
    elif len(sys.argv) >= 5:
        print("ERROR: too many arguments")
        argument_list()
        return True
    else:
        var_1 = float(sys.argv[2])
        var_2 = float(sys.argv[3])
        if var_1 <= 0 or var_2 <= 0:
            print("ERROR: enter positive values")
            return False
        else:
            return True

def area_circle():
    """
    Prints the area for a circle based on radius
    """
    if input_validation_1_measure():
        radius = float(sys.argv[2])
        area = radius * math.pi
        print(area)

def area_square():
    """
    Prints the area for a square based on side
    """
    if input_validation_1_measure():
        side = float(sys.argv[2])
        area = side**2
        print(area)

def area_quadrilateral():
    """
    Prints the area for rhombus and rectangle, product of base and side
    """
    if input_validation_2_measures():
        base = float(sys.argv[2])
        height = float(sys.argv[3])
        area = base * height
        print(area)

def area_triangle():
    """
    Prints the area for triangle based on base and height
    """
    if input_validation_2_measures():
        base = float(sys.argv[2])
        height = float(sys.argv[3])
        area = base * height / 2
        print(area)

# Sends an error message if missing command line arguments
if len(sys.argv) <= 2:
    print("ERROR: command line arguments missing")
    pass

# Reads the name of the shape and apply the corresponding area calculation
# function
else :
    name_shape = str(sys.argv[1]).lower()
    if name_shape == "circle":
        area_circle()
    elif name_shape in ["rectangle", "rhombus"]:
        area_quadrilateral()
    elif name_shape == "triangle":
        area_triangle()
    elif name_shape == "square":
        area_square()
    else:
        print("ERROR: enter a valid shape name")
