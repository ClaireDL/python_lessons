#!/usr/bin/env python


def insertsort(xs):
    """
    Compares input element to be sorted with last value in the sorted list
    If input element is inferior, last value is shifted to the right to make
    space for input element.
    Until input element is larger
    """

    i = 1

    for i, _ in enumerate(xs):
        current_element = xs[i]
        last_element = xs[i - 1]
        if current_element <= last_element:
            xs[i] = xs[i - 1]
    return xs


print(insertsort([2 , 6 , 3 , 15 , 12]))
