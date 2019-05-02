#!/usr/bin/env python

import time

def calculate_execution_time(pre, post):
    execution_time = float(post - pre)
    return execution_time

def collect_data_for_graph(list_size, execution_time):
    data_list = []
    data_list.append([list_size, execution_time])
    return data_list
