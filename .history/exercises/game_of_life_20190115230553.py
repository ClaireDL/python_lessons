#!/usr/bin/env python

import random

def initialise_field(width_local, height_local):
    """
    Seed stage
    Initialises, e.g. populates, a field with a population of randomly selected alive
    (1) or dead (0) cells
    """
    return [[random.randint(0, 1) for i in range(width_local)] for y in range(height_local)]


# FIXME: What is "z"??? That's not meaningful
def get_cell_status(z):
    """
    List of parameters:
    Any live cell with fewer than two live neighbours dies, as if by under-
    Any live cell with two or three live neighbours lives on to the next
    generation.
    population.
    Any live cell with more than three live neighbours dies (overpopulation)
    Any dead cell with exactly three live neighbours becomes a live cell
    (reproduction)
    """

def get_neighbour_positions(my_field):
    """
    Returns the position of a cell's neighbours as a list
    """
    neighbours = []
    for line in range(0, len(my_field)):
        index_line = int(line)
        for item in range(0, line):
            index_cell = int(item)
            neighbour_1 = index_line - 1
            neighbour_2 = index_line + 1
            neighbour_3 = my_field[index_line - 1][index_cell - 1]
            neighbour_4 = my_field[index_line - 1][index_cell]
            neighbour_5 = my_field[index_line - 1][index_cell + 1]
            neighbour_6 = my_field[index_line + 1][index_cell - 1]
            neighbour_7 = my_field[index_line + 1][index_cell]
            neighbour_8 = my_field[index_line + 1][index_cell + 1]
            # adds to the list the neighbours of a cell
            neighbours.append([neighbour_1, neighbour_2,
            neighbour_3, neighbour_4, neighbour_5, neighbour_6,
            neighbour_7, neighbour_8])
    return neighbours


# Defines the dimensions of the field
width = 7
height = 10
field = initialise_field(width, height)
print(field)

# displays the field line by line
for y in range(height):
    print(field[y])

print(get_neighbour_positions(field))
