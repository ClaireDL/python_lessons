#!/usr/bin/env python

import random

def initialise_field(width_local, height_local):
    """
    Seed stage
    Initialises, e.g. populates, a field with a population of randomly selected alive
    (1) or dead (0) cells
    """
    my_field = []
    my_field = [[random.randint(0, 1) for i in range(width_local)] for y in range(height_local)]
    return my_field

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

def get_neighbour_positions(my_list):
    """
    Returns the position of a cell's neighbours as a list
    """
    neighbours = []
    for nested in range(0, len(my_list)):
        for item in nested:
            # previous line
            prev_line1 = my_list[nested - 1][item - 1]
            prev_line2 = my_list[nested - 1][item])
            prev_line3 = my_list[nested - 1][item + 1])
            # next t
            line1 = my_list[nested + 1][item - 1])
            line2 = my_list[nested + 1][item])
            line3 = my_list[nested + 1][item + 1])
            # same t
            line = my_list[nested][item - 1])
            line = my_list[nested][item + 1])
    return neighbours

# Defines the dimensions of the field
width = 7
height = 10
field = initialise_field(width, height)

# displays the field line by line
for y in range(height):
    print(field[y])

cell_neighbours = get_neighbour_positions(field)
