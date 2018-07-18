#!/usr/bin/env python

import math
import sys
import random

def gaussian_function(x, mean,sd):
    """
    Gaussian function for a given abcisse, mean and standard deviation
    """
    x = random.random(-sys.maxint, sys.maxint)
    factor = 1/math.sqrt(2 * math.pi * sd**2)
    exponent = -(x - mean)**2/(2 * sd**2)
    exponentialfunction = math.pow(math.e,exponent)
    return factor * exponentialfunction

average = float(sys.argv[2])
standarddeviation = float(sys.argv[3])

print(x_abcisse)
print(gaussian_function(x_abcisse, average, standarddeviation))