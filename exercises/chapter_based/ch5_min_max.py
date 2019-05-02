#!/usr/bin/env python

# Given a list of numbers find the min and max without using built-in min() and
# max()

import operator

list1 = [2, 48, 3, 4, 7, 14, 5, 36, 9]

# Verification, using built-in functions
print("min is %i and max is %i " % (min(list1), max(list1)))

# solution 1
# NOT A GOOD SOLUTION BECAUSE OF COMPLEXITY: THERE IS NO NEED TO SORT THE LIST
# sorts the list
list1_sorted = sorted(list1)

# gets the minimum, first position in the ordered list, and maximum, last
# position in the ordered list
minimum = list1_sorted[0]
maximum = list1_sorted[len(list1_sorted) - 1]
print("min is %i and max is %i " % (minimum, maximum))

# solution 2
#
def find_maximum(xs):
    """
    From an input list, returns the element with the biggest value
    Returns None for an empty list
    """
    if xs == []:
        return None
    maximum =  xs[0]
    for element in xs:
        if element >= maximum:
            maximum = element
    return maximum

def find_minimum(xs):
    """
    From an input list, returns the element with the smallest value
    Returns None for an empty list
    """
    minimum = None
    for element in xs:
        if element is None or element <= minimum:
            minimum = element
    return minimum

def find_value(xs, operator):
    """
    From an input list and operator (minimum, maximum)
    returns the required value
    Returns None for an empty list
    """
    if xs == []:
        return None
    value = xs[0]

    for element in xs:
            if value_type == "minimum":
                if operator.le(element, value)
                value = element
            elif value_type == "maximum":
                if operator.ge(element, value)
                value = element
        return value


#
# Unit test
#   Requires installation of package unittest2
#   Run using: python -m unittest ch5_minmax
#

import unittest

class MaxTest(unittest.TestCase):

    def test_empty_list(self):
        result = find_maximum([])
        self.assertEquals(result, None)

    def test_single_element(self):
        result = find_maximum([1])
        self.assertEquals(result, 1)

    def test_increasing_list(self):
        result = find_maximum([1, 2, 3, 4, 5])
        self.assertEquals(result, 5)

    def test_decreasing_list(self):
        result = find_maximum([5, 4, 3, 2, 1])
        self.assertEquals(result, 5)

    def test_updown_list(self):
        result = find_maximum([1, 2, 3, 2, 1])
        self.assertEquals(result, 3)

    def test_downup_list(self):
        result = find_maximum([3, 2, 1, 2, 3 ])
        self.assertEquals(result, 3)


class MinTest(unittest.TestCase):

    def test_empty_list(self):
        result = find_minimum([])
        self.assertEquals(result, None)

    def test_single_element(self):
        result = find_minimum([1])
        self.assertEquals(result, 1)

    def test_increasing_list(self):
        result = find_minimum([1, 2, 3, 4, 5])
        self.assertEquals(result, 1)

    def test_decreasing_list(self):
        result = find_minimum([5, 4, 3, 2, 1])
        self.assertEquals(result, 1)

    def test_updown_list(self):
        result = find_minimum([1, 2, 3, 2, 1])
        self.assertEquals(result, 1)

    def test_downup_list(self):
        result = find_minimum([3, 2, 1, 2, 3 ])
        self.assertEquals(result, 1)
