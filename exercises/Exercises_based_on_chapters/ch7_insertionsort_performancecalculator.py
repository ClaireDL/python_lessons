#!/usr/bin/env python

from ch5_insertsort2 import insertsort
from ch7_calculator import calculate_execution_time, collect_data_for_graph
import sys
import random
import time

def generate_random_list():
    """
    Returns a random sized-list of random integers (upper limit is fixed to 10K)
    """
    return [random.randint(0, 10000) for i in range(random.randint(0, 10000))]

for i in range(0, 10):
    timestamp_pre = time.time()
    list_to_sort = generate_random_list()
    # runs insertion sort
    insertsort(list_to_sort)
    timestamp_post = time.time()

    # calls a program to calculate execution time
    execution_time = calculate_execution_time(timestamp_pre, timestamp_post)
    # calls a program that gathers information about program execution, list size and execution time
    print(collect_data_for_graph(len(list_to_sort), execution_time))


