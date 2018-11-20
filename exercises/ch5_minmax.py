#!/usr/bin/env python

# Given a list of numbers find the min and max without using built-in min() and
# max()

list1 = [2, 48, 3, 4, 7, 14, 5, 36, 9]

# Verification, using built-in functions
print("min is %i and max is %i " % (min(list1), max(list1)))

# solution 1
# sorts the list
list1_sorted = sorted(list1)

# gets the minimum, first position in the ordered list, and maximum, last
# position in the ordered list
minimum = list1_sorted[0]
maximum = list1_sorted[len(list1_sorted) - 1]
print("min is %i and max is %i " % (minimum, maximum))
