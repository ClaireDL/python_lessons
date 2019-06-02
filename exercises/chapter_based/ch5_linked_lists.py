#!/usr/bin/env python

def empty():
    return []

def prepend(item, linked_list):
    return [item, linked_list]

def head(linked_list):
    return linked_list[0]

def tail(linked_list):
    return linked_list[1]

def is_linked_list(test_var):
    if not isinstance(test_var, list):
        return False
    if len(test_var) > 2:
        return False
    if len(test_var) == 0:
        return True
    if len(test_var) == 1:
        return False
    if len(test_var) == 2:
        return is_linked_list(test_var[1])

## this is not a primitive because it can be implemented using the others
def is_empty(linked_list):
    return linked_list == empty()

a = prepend(1, prepend(2, prepend(3, empty())))
print(is_linked_list(a))

print(head(a))
