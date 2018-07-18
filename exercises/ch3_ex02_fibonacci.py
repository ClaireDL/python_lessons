#!/usr/bin/env python

def fibonacci(number):
    """
    Recursive function to calculate the Fibonacci sequence
    """
    if number == 0:
        return 0
    return fibonacci(number - 1) + number

print(fibonacci(5))