#!/usr/bin/env python

import math
import sys
import random

def gaussian_num_generator():
    """
    Returns 1 random number that follows a Gaussian distribution
    Uses the Box-Muller transform with 2 uniformly distributed [0;1[ numbers
    ref: Thomas, Luk, Leong & Villasenor (2007)
    """
    a = random.random()
    b = random.random()
    trans_a = math.sqrt(-2 * math.log(a))
    trans_b = 2 * math.pi * b
    return trans_a * math.sin(trans_b)

print(gaussian_num_generator())
