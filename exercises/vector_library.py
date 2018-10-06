#!/usr/bin/env python

import math


def vector_addition(v1, v2):
    """
    Returns the coordinates of the resultant vector after an addition
    """
    resultant_x = v1[0] + v2[0]
    resultant_y = v1[1] + v2[1]
    return [resultant_x, resultant_y]


def vector_substraction(v1, v2):
    """
    Returns the coordinates of the resultant vector after a substraction
    """
    resultant_x = v1[0] - v2[0]
    resultant_y = v1[1] - v2[1]
    return [resultant_x, resultant_y]


def vector_scalar_multiplication(v1, a):
    """
    Returns the resultant vector coordinates of a scalar multiplication
    """
    resultant_x = v1[0] * a
    resultant_y = v1[1] * a
    return [resultant_x, resultant_y]


def vector_multiplication_dot_product(v1, v2):
    """
    Returns the resultant vector coordinates of a dot product
    """
    resultant_x = v1[0] * v2[0]
    resultant_y = v1[1] * v2[1]
    return [resultant_x, resultant_y]


def vector_multiplication_cross_product(v1, v2):
    """
    Returns the 3 dimensional resultant vector of a cross product from 2 dimensional vectors
    """
    xs = []
    angle_cross_product = angle_v(v1) - angle_v(v2)
    magnitude_cross_product = magnitude_v(v1) * magnitude_v(v2) * math.degrees(math.sin(angle_cross_product))
    return coordinates_v(magnitude_cross_product, t = 90)


def magnitude_v(v1):
    """
    Returns the magnitude of a vector from its coordinates
    """
    magnitude = math.sqrt(math.pow(v1[0], 2) + math.pow(v1[1], 2))
    return magnitude


def angle_v(v1):
    """
    Returns the angle of a vector form its coordinates
    """
    angle = math.degrees(math.atan(v1[1] / v1[0]))
    return angle


def coordinates_v(l, t):
    """
    Returns the x y coordinates of a vector based on its length and angle
    """
    length = magnitude_v(l)
    theta = angle_v(t)
    abcissa = length * math.degrees(math.cos(theta))
    ordinate = length * math.degrees(math.sin(theta))
    return [abcissa, ordinate]


# A vector is defined by its coordinates when the tail is at the origin
vector_1 = [4, 3]
vector_2 = [2, 5]
scalar = 3

print("The resultant of vector addition is %s." % vector_addition(vector_1, vector_2))
print("The resultant of vector substraction is %s." % vector_substraction(vector_1, vector_2))
print("The resultant of scalar multiplication is %s." % vector_scalar_multiplication(vector_1, scalar))
print("The dot product of 2 vectors is %s." % vector_multiplication_dot_product(vector_1, vector_2))

print(vector_multiplication_cross_product(vector_1, vector_2))
