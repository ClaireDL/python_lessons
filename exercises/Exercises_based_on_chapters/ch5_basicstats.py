#!/usr/bin/env python

import math


def sum(xs):
    """
    Returns the sum of numbers contained in a list
    """

    result = 0.0

    for current_element in xs:
        result += current_element
    return result


def average(xs):
    """
    Returns the average of numbers contained in a list
    """

    result = 0.0
    samplesize = len(xs)

    for current_element in xs:
        result += current_element
    return result / samplesize


def sd(xs):
    """
    Returns the standard deviation of a list of numbers
    """
    deviation_list = []

    for current_element in xs:
        deviation = (current_element - average(xs)) ** 2
        deviation_list.append(deviation)
    return average(deviation_list)


def one_sample_t_value(xs, mu):
    """
    Returns the T value for a T-test for numbers in a list and
    the reference value
    """

    mean = average(xs)
    stdev = sd(xs)
    samplesize = len(xs)

    return (mean - mu)/(stdev / math.sqrt(samplesize))

print(sum([2, 5]))
print(average([2, 5]))
print(sd([2, 7, 3]))
print(one_sample_t_value([2, 7, 4, 12], 15))
