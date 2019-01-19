#!/usr/bin/env python

import sys

def fizzbuzz(number):
    """
    This function returns fizz if a given number is a multiple of 3,
    buzz if it is a multiple of 5 and fizz buzz if it's a multiple of both.
    """

    if number%3 == 0 and number%5 == 0:
        return "Fizz Buzz"
    elif number%3 == 0:
        return "Fizz"
    elif number%5 == 0:
        return "Buzz"

number = int(sys.argv[1])
print(fizzbuzz(number))