#!/usr/bin/env python

import random

def initialise_field(width_local, height_local):
    """
    Seed stage
    Initialises, e.g. populates, a field with a population of randomly selected alive
    (1) or dead (0) cells
    """
    return [[random.randint(0, 1) for i in range(width_local)] for y in range(height_local)]

def iterate_through_field(field):
    """
    Goes through each cell of the field with two indexes
    for row and column number
    """

    def get_neighbours(row, col):
        """
        Returns the neighbours of a cell
        """
        neighbour_index_list = []
        neighbour_index_list.append([
            [row - 1, col - 1],
            [row - 1, col],
            [row - 1, col + 1],
            [row, col - 1],
            [row, col + 1],
            [row + 1, col - 1],
            [row + 1, col],
            [row + 1, col + 1],
        ])
        return neighbour_index_list

    for row in range(len(field)):
        for col in range(len(field[row])):
            index_neighbours = get_neighbours(row, col)
            for cell in index_neighbours:
                print(cell)

# MAIN PROGRAM STARTS HERE
# Defines the dimensions of the field
width = 7
height = 10
field = initialise_field(width, height)

# print(field)

# displays the field as an array
#    for line in range(height):
#        print(field[line])
#    print()

#    print(iterate_through_field(field))

# testing
test_field = [
    [0, 1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12, 13],
    [14, 15, 16, 17, 18, 19, 20]
]

#for test_line in test_field:
#    print(test_line)

iterate_through_field(test_field)
print(test_field[-1][1])
