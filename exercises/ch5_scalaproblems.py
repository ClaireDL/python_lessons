#!/usr/bin/env python

list_1 = [1, 1, 2, 3, 5, 8]

# Problem 1
# Find last element of a list

# solution 1
last_element = list_1[-1]
print("The last element of the list is %i." % last_element)

# solution 2
last_element2 = list_1[len(list_1)-1]
print("The last element of the list is %i." % last_element2)

# solution 3


def last_element(xs):
    if len(xs) == 1:
        return xs
    return last_element(xs[1:])


final_list_last = last_element(list_1)
print("The last element of the list is %i." % final_list_last[0])


# Problem 2
#  Find the last but one element of a list
last_but_one = list_1[-2]
print("The last but one element of the list is %s." % last_but_one)

# solution 2
last_element2 = list_1[len(list_1)-2]
print("The last but one element of the list is %s." % last_element2)

# solution 3


def last_element_but_one(xs):
    if len(xs) == 2:
        return xs
    return last_element_but_one(xs[1:])


final_list_last_but_one = last_element_but_one(list_1)
print("The last element but one of the list is %i." % final_list_last_but_one[0])

# Problem 3
# Find the Kth element of a list.

# solution 1
kth_element = input("Enter the index number of the element you want: ")
if kth_element > len(list_1):
    print("This is not a valid index, too big.")
else:
    print("The Kth element of the list is %i." % list_1[kth_element])

# Problem 4
# Find the number of elements of a list

# solution 1
print("The list contains %i elements." % len(list_1))

# Problem 5
# Reverse a list

# solution 1


def reverse_recursive(xs):
    if xs == []:
        return []
    return reverse_recursive(xs[1:]) + [xs[0]]


print("The reverse list is: %s" % reverse_recursive(list_1))

# solution 2


def reverse_for_loop(xs):
    list_reverse = []
    for current_element in xs:
        list_reverse.insert(0, current_element)
    return list_reverse

print("The reverse list is: %s" % reverse_for_loop(list_1))

# solution 3


def reverse_new_list(xs):
    new_list = list(xs)
    for i in range(0, len(xs)):
        index = len(xs) - i - 1
        new_list[index] = xs[i]
    return new_list

print(reverse_new_list(list_1))

# Problem 6
# Find out whether a list is a palindrome

# solution 1


def palindrome_list(xs):
    reverse_list = reverse_recursive(xs)
    if reverse_list == xs:
        return True
    else:
        return False


list_2 = [1, 2, 3, 2, 1]
print(palindrome_list(list_2))

# solution 2


def palindrome_list_for_loop(xs):
    reverse_list = reverse_recursive(xs)
    for current_element in xs:
        if reverse_list[current_element] == xs[current_element]:
            return True
        else:
            return False


print(palindrome_list_for_loop(list_2))

# solution 3

def palindrome_list_iterative(xs):
    new_list = list(xs)
    for i in range(0, len(xs)):
        index = len(xs) - i - 1
        if new_list[index] == xs[i]:
            return True
        else:
            return False

print(palindrome_list_iterative(list_2))
