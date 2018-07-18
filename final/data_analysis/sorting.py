#!/usr/bin/env python


def insertion(items):
    """
    Insertion sort
    """
    items = list(items)
    for i in range(len(items)):
        for j in range(len(items)):
            if items[j] > items[i]:
                items[j], items[i] = items[i], items[j]

    return items


def merge(items):
    """
    Merge sort
    """
    def recurse(items):
        if len(items) <= 1:
            # When arrived at the end we have nothing to do
            return
        else:
            # Subsorting of the two halves of the list
            mid = len(items) // 2
            recurse(items[:mid])
            recurse(items[mid:])

            # Merging of the sorted halves
            i, j = 0, 0
            while i < mid and j < len(items[mid:]):
                if items[i] > items[mid + j]:
                    items[i], items[mid + j] = items[mid + j], items[i]
                    j += 1
                else:
                    i += 1

    # Start the sorting with a copy of the input list
    return recurse(list(items))
