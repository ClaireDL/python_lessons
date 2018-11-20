#!/usr/bin/env python

# Exercise: generate a script that transform a list of nested lists into one list

list1 = [[2, 4, 5], [12, 4, 7], [1, 4]]
newlist = []
for current_element in list1:
    newlist.extend(current_element)
print(newlist)
