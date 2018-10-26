#!/usr/bin/env python

# Exercise: generate a script that transform a list of nested lists into one list

list1 = [[2, 4, 5], [12, 4, 7], [1, 4]]
print(len(list1))
newlist = []
for current_element in list1:
    for i in range(len(current_element)):
        newlist.append(current_element[i])
print(newlist)
