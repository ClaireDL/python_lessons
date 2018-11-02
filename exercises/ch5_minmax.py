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

# solution 2
# sorts list in ascending order
list1_min = sorted(list1)
# minimum is the first value in the list
minimum = list1_min[0]
# sorts list in descending order
list1_max = sorted(list1, reverse=True)
# maximum is the first value in the list
maximum = list1_max[0]
print("min is %i and max is %i " % (minimum, maximum))
