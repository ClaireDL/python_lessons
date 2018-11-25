#!/usr/bin/env python

# Given a list of numbers find the min and max without using built-in min() and
# max()

list1 = [2, 48, 3, 4, 7, 14, 5, 36, 9]

# Verification, using built-in functions
print("min is %i and max is %i " % (min(list1), max(list1)))

# solution 1
# NOT A GOOD SOLUTION BECAUSE OF COMPLEXITY: THERE IS NO NEED TO SORT THE LIST
# sorts the list
list1_sorted = sorted(list1)

# gets the minimum, first position in the ordered list, and maximum, last
# position in the ordered list
minimum = list1_sorted[0]
maximum = list1_sorted[len(list1_sorted) - 1]
print("min is %i and max is %i " % (minimum, maximum))

# solution 2
#
def find_maximum(xs):
    """
    This function compares elements from the list in pairs.
    THe bigger of the two elements remains and is compared with next element in
    the list.
    """
    element = xs[0]
    for i in range(1, len(list1)):
        if element > xs[i]:
            return element
        element = xs[i]
    return element

def find_minimum(xs):
    """
    This function compares elements from the list in pairs.
    The smaller of the two elements remains and is compared with next element in
    the list.
    """
    element = xs[0]
    for i in range(1, len(list1)):
        if element < xs[i]:
            return element
        element = xs[i]
    return element

max = find_maximum(list1)
min = find_minimum(list1)
print("min is %i and max is %i " % (min, max))
