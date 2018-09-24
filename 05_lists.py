#!/usr/bin/env python

# Just imports print_function from the package future
from __future__ import print_function

# Empty list
list_1 = []

# List of numbers
list_2 = [1, 3, 5, 7]
print(list_2)

# Changing element #1
list_2[1] = 10
print(list_2)

# Length
print(len(list_2))

# Mixed list
list_3 = [["a", "b"], True, 123, None, "hello"]
print(list_3)

# Printing element #1
print("Element #1: %s" % list_3[1])

# List contain references
element_0 = list_3[0]
print(element_0)
element_0[1] = "C"
print(element_0)
print(list_3)

# Add element
list_2.append(123)
print(list_2)

list_2.insert(0, 321)
print(list_2)

# Join two lists
list_2.extend([8, 6, 4])
print(list_2)

# Strings are lists (of characters)
my_name = "Fabrizio"
print(my_name[2])

# Getting subsets
print(list_2[3:5])
print(list_2[:5])
print(list_2[3:])
print(my_name[3:5])

# Join and split strings
users_i_like = "fabrizio,claire,bibi,jake"
print("Original string: %s" % users_i_like)
users_list = users_i_like.split(',')
print(users_list)
print("The users I like are:")
nice_list = '\n'.join(users_list)
print(nice_list)

# Recursion with lists
def reverse_rec(xs):
    if xs == []:
        return []
    return reverse_rec(xs[1:]) + [xs[0]]

# Unit testing
print(reverse_rec([]))
print(reverse_rec([2]))
print(reverse_rec([2, 6, 3, 8]))
print("")

# The same with loops!
def reverse_iter(xs):
    result = []
    for current_element in xs:
        result.insert(0, current_element)
    return result

print(reverse_iter([]))
print(reverse_iter([2]))
print(reverse_iter([2, 6, 3, 8]))
print("")

# The "C" way, using index
def reverse_index(xs):
    result = list(xs)
    for i in range(len(xs)):
    #for i, _ in enumerate(xs):
        result[len(result) - 1 - i] = xs[i]
    return result

print(reverse_index([]))
print(reverse_index([2]))
print(reverse_index([2, 6, 3, 8]))
print("")

# Minimum and maximum
print("Maximum: %s" % max(list_2))
print("Minimum: %s" % min(list_2))
print("Sum: %s" % sum(list_2))

# Filtering
def is_odd(number):
    return number % 2 != 0
print("Only odd numbers: %s" % filter(is_odd, list_2))
print("Only odd numbers: %s" % filter(lambda n: n % 2 != 0, list_2))

# Mapping
result = map(lambda n: "This is number %s" % n, list_2)
print(result)

# Sorting
result = sorted(list_2)
print(result)

# Sorting in reverse
result = sorted(list_2, reverse=True)

# I can also use a custom sorting function
def my_custom_comparison(x1, x2):
    # This sorts in reverse order
    if x1 > x2:
        return -1
    elif x1 == x2:
        return 0
    elif x1 < x2:
        return 1
    # Can be shortened in
    return x1 - x2

result = sorted(list_2, my_custom_comparison)
# And the custom sorting function in one line
result = sorted(list_2, lambda x1, x2: x2 - x1)
print(result)
