#!/usr/bin/env python


def insertsort(xs):
    """
    Assumes that the first element in the list is sorted. This is the minimal
    sorted sublist.
    Evaluates subsequent elements in the list incrementally.
    It considers one element and a current position:
    If element is smaller than the value to its left, their places are exchanged
    (element is put to the previous position).
    Until element is no longer smaller and element is in the initial position
    in the list.
    This is then its sorted position.

    The process is repeated for all the elements in the list.

    Returns the sorted list.
    """

    for index in range(1, len(xs)):
        element = xs[index]
        current_position = index
        while current_position > 0 and xs[current_position - 1] > element:
            xs[current_position] = xs[current_position - 1]
            current_position = current_position - 1
        xs[current_position] = element
    return xs


input_list = [5, 4, 6, 1, 7, 2, 3, 9, 8]
result = insertsort(input_list)
# print(result)
