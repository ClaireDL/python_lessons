#!/usr/bin/env python

from ch5_insertsort2 import insertsort
import sys
import time
import random


def generate_random_list(size):
    """
    Returns a random sized-list of random integers (upper limit is fixed to 10K)
    """
    size = int(size)
    return [random.randint(0, 100) for i in range(size)]

list_size = [x * x for x in range(100)]

timedata = []
for i in range(len(list_size)):
    my_list = generate_random_list(list_size[i])
    time_pre = time.time()
    my_list_sorted = insertsort(my_list)
    time_post = time.time()
    execution_time = time_post - time_pre
    timedata.append([list_size[i], execution_time])

for i in range(len(timedata)):
    print(timedata[i])
