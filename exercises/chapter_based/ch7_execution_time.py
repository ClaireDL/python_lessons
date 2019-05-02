#!/usr/bin/env python

from ch5_insertsort2 import insertsort
from datetime import datetime
from time import time, clock
import random
import sys


def generate_random_list(size):
    """
    Returns a list with random integers
    """
    return [random.randint(0, 100) for i in range(size)]

samples_sizes = [x * x for x in range(30)]

timedata = []
for sample_size in samples_sizes:
    sample = generate_random_list(sample_size)
    #time_pre = time()
    time_pre = clock()
    sample_sorted = insertsort(sample)
    #time_post = time()
    execution_time = (clock() - time_pre)
    time_post = clock()
    print("sample size: %i execution time %f" %(sample_size, execution_time))
    timedata.append([sample_size, execution_time])

#print(timedata)
