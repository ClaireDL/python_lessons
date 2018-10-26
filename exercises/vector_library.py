#!/usr/bin/env python

import math

def get_terminal_point(v1):
    """
    Gets the terminal point of free and applied vectors.
    """
    if len(v1) == 2:
        return v1
    elif len(v1) == 4:
        abcissa = v1[0] + v1[2]
        ordinate = v1[1] + v1[3]
        return [abcissa, ordinate]

def add(v1, v2):
    """
    Performs vector addition.
    Returns the resultant vector coordinates.
    """
    v1 = get_terminal_point(v1)
    v2 = get_terminal_point(v2)
    result_x = v1[0] + v2[0]
    result_y = v1[1] + v2[1]
    return [result_x, result_y]


def subtract(v1, v2):
    """
    Performs vector subtraction.
    Returns the resultant vector coordinates.
    """
    v1 = get_terminal_point(v1)
    v2 = get_terminal_point(v2)
    result_x = v1[0] - v2[0]
    result_y = v1[1] - v2[1]
    return [result_x, result_y]


def multiply_scalar(v1, magnitude_scalar):
    """
    Performs vector multiplication by a scalar.
    Returns the resultant vector coordinates.
    """
    v1 = get_terminal_point(v1)
    result_x = v1[0] * magnitude_scalar
    result_y = v1[1] * magnitude_scalar
    return [result_x, result_y]


def multiply_dotproduct(v1, v2):
    """
    Performs dot product multiplication.
    Returns the resultant vector coordinates.
    """
    v1 = get_terminal_point(v1)
    v2 = get_terminal_point(v2)
    angle_v1 = calculate_angle(v1)
    angle_v2 = calculate_angle(v2)
    if angle_v1 - angle_v2 == 90:
        return 0
    else:
    result = v1[0] * v2[0] + v1[1] * v2[1]
    return result


def multiply_crossproduct(v1, v2):
    """
    Performs cross product multiplication.
    Returns the resultant vector coordinates.
    """
    angle_v1 = calculate_angle(v1)
    angle_v2 = calculate_angle(v2)
    magnitude_v1 = calculate_magnitude(v1)
    magnitude_v2 = calculate_magnitude(v2)

    if angle_v1 == angle_v2:
        return 0
    else:
        angle_crossprod = angle_v1 - angle_v2
        magnitude_crossprod = magnitude_v1 * magnitude_v2 * math.degrees(math.sin(angle_crossprod))
        result = calculate_coordinates(magnitude_crossprod, angle_crossprod)
        return result


def calculate_magnitude(v1):
    """
    Returns the magnitude of a vector from its coordinates
    """
    magnitude = math.sqrt(math.pow(v1[0], 2) + math.pow(v1[1], 2))
    return magnitude


def calculate_angle(v1):
    """
    Returns the angle of a vector form its coordinates
    """
    angle = math.degrees(math.atan(v1[1] / v1[0]))
    return angle


def calculate_coordinates(magnitude, angle):
    """
    Returns the x y coordinates of a vector based on its magnitude and angle
    """
    v1 = get_terminal_point(v1)
    theta = calculate_angle(v1)
    abcissa = calculate_magnitude(v1) * math.degrees(math.cos(theta))
    ordinate = calculate_angle(v1) * math.degrees(math.sin(theta))
    return [abcissa, ordinate]


# A free vector is defined by its coordinates when the tail is at the origin
vector_1 = [4, 3]
vector_2 = [2, 5]

# Scalar for scalar multiplication
scalar = 3

# An applied vector is defined by its x y coordinates
# followed by the x y coordinates of the tail
applied_vector_1 = [4, 3, 1, 2]
applied_vector_2 = [2, 5, -1, -1]

addition = add(vector_1, vector_2)
print("The result of vector addition is %s." % addition)

addition = add(applied_vector_1, applied_vector_2)
print("The result of vector addition is %s." % addition)

subtraction = subtract(vector_1, vector_2)
print("The result of vector subtraction is %s." % subtraction)

multiplication = multiply_scalar(vector_1, scalar)
print("The result of scalar multiplication is %s." % multiplication)

dotproduct = multiply_dotproduct(vector_1, vector_2)
print("The dot product of the 2 vectors is %s." % dotproduct)

#crosssproduct = multiply_crossproduct(vector_1, vector_2)
#print("The dot product of 2 vectors is %s." % crossproduct)
