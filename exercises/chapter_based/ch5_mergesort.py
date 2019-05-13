#!/usr/bin/env python

def mergesort(xs):
    """
    Split the unsorted list into sublists until there are lists with 1 element only
    Sorts elements in a list of 2 elements
    """
    middle = len(xs)//2
    left_array = xs[0:middle]
    right_array = xs[middle:]
    if middle == 0:
        return xs
    # recursively splits lists into two halves
    left_array = mergesort(left_array)
    right_array = mergesort(right_array)
    xs = left_array + right_array
    # calls the merge function
    sortmerge(xs, middle, len(xs))
    return xs

def sortmerge(half, cutpoint, total_length):
    """
    Compares two adjacent elements then merge them
    """
    left = []
    right = []

    for i in range(cutpoint):
        left.append(half[i])
    for j in range(total_length - cutpoint):
        right.append(half[cutpoint + j])

    left.append("null")
    right.append("null")

    k = 0
    l = 0
    for i in range(total_length):
        if left[k] < right[l]:
            half[i] = left[k]
            k += 1
        else:
            half[i] = right[l]
            l += 1
    return half

# print("this is the unsorted list")
# input_list = [5, 4, 6, 1, 7, 2, 3, 9, 8]
# print(input_list)
# result = mergesort(input_list)
# print("this is merge sort")
# print(result)
