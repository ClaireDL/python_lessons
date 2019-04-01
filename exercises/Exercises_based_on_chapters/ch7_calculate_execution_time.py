#!/usr/bin/env python

import ch5_insertsort2
import sys
import random
import time

def generate_random_list():
    """
    Returns a random sized-list of random integers (upper limit is fixed to 10K)
    """
    return [random.randint(0, 10000) for i in range(random.randint(0, 10000))]

def collect_execution_timedata():
    """
    Returns a list comprising of the length of a listand the time
    necessary to run an insert-sort algorithm
    """
    time_pre = time.time()
    my_list = generate_random_list()
    ch5_insertsort2.insertsort(my_list)
    time_post = time.time()
    execution_time = time_post - time_pre
    return [len(my_list), execution_time]

timedata = []
for i in range(0, 100):
    timedata.append(collect_execution_timedata())

print(timedata)
