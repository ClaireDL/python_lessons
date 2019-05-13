#!/usr/bin/env python

from ch5_insertsort2 import insertsort
from ch5_mergesort import mergesort
from datetime import datetime
from time import time, clock
import random
import sys


def generate_random_list(size):
    """
    Returns a list with random integers
    """
    return [random.randint(0, 100) for i in range(size)]

samples_sizes = [x * x for x in range(50)]

timedata = []
for sample_size in samples_sizes:
    sample = generate_random_list(sample_size)
    #time_pre = time()
    time_pre = clock()
    sample_sorted = insertsort(sample)
    #time_post = time()
    time_post = clock()
    execution_time = (clock() - time_pre)
    timedata.append([sample_size, execution_time])

with open("insertsort.txt", "w+") as result_insertsort:
    result_insertsort.writelines("Insert sort\n")
    result_insertsort.writelines("sample size\texecutiontime\n")
    for line in timedata:
        result_insertsort.writelines("%i\t%f\n" % (line[0], line[1]))

with open("insertsort.txt", "r") as result_insertsort:
    print(result_insertsort.read())
