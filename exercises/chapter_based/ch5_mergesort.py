#!/usr/bin/env python


def mergesort(xs):
    """
    Sorts the input list
    """
    if len(xs) <= 1:
        return xs

    # splits the input list in two halves
    middle = len(xs) // 2
    left_array = xs[:middle]
    right_array = xs[middle:]

    # sorts each half
    left_array = mergesort(left_array)
    right_array = mergesort(right_array)

    #
    xs = left_array + right_array

    # merges the two sorted halves
    merge(xs, middle, len(xs))
    return xs


#def merge(left_list, right_list):
def merge(to_merge, cutpoint, total_length):
    """
    Merge function of the merge sort algorithm
    Merges two sorted list so that the output list is itself sorted
    """
    left = []
    right = []

    for i in range(cutpoint):
        left.append(to_merge[i])
    for j in range(total_length - cutpoint):
        right.append(to_merge[cutpoint + j])

    left.append("null")
    right.append("null")

    k = 0
    l = 0
    for i in range(total_length):
        if left[k] < right[l]:
            to_merge[i] = left[k]
            k += 1
        else:
            to_merge[i] = right[l]
            l += 1
    return to_merge

# print("this is the unsorted list")
# input_list = [5, 4, 6, 1, 7, 2, 3, 9, 8]
# print(input_list)
# result = mergesort(input_list)
# print("this is merge sort")
# print(result)
