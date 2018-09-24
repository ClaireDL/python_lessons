#!/usr/bin/env python

list_1 = [1, 1, 2, 3, 5, 8]

# Problem 1
# Find last element of a list

# solution 1
last_element = list_1[-1]
print("The last element of the list is %s." % last_element)

# solution 2
last_element2 = list_1[len(list_1)-1]
print("The last element of the list is %s." % last_element2)

# Problem 2
#  Find the last but one element of a list
last_but_one = list_1[-2]
print("The last but one element of the list is %s." % last_but_one)

# Problem 3
# Find the Kth element of a list.
kth_element = input("Enter the index number of the element you want: ")
if kth_element > len(list_1):
    print("This is not a valid index, too big.")
else:
    print("The Kth element of the list is %i." % list_1[kth_element])
