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
    for nested in my_field:
        for item in nested:
            if item % len(nested -1) == 0:
                neighbours.append(myfield[nested - 1][nested - 1]
                neighbours.append(myfield[nested][nested - 1]
                neighbours.append(myfield[nested + 1][nested - 1]
            else:
                neighbours.append(myfield[nested - 1][item - 1]
                neighbours.append(myfield[nested][item - 1]
                neighbours.append(myfield[nested + 1][item - 1]
            if item % len(nested -1) == len(nested) - 1:
                neighbours.append(myfield[nested - 1][0])
                neighbours.append(myfield[nested][0])
                neighbours.append(myfield[nested + 1][0])
            else:
                neighbours.append(myfield[nested - 1][item + 1])
                neighbours.append(myfield[nested][item + 1])
                neighbours.append(myfield[nested + 1][item + 1])

            neighbours.append(myfield[nested - 1][item + 1])
            neighbours.append(myfield[nested][item + 1])
            neighbours.append(myfield[nested + 1][item + 1])

            neighbours.append(myfield[nested - 1][item]
            # same line
            # next line
            neighbours.append(myfield[nested + 1][item]


# Defines the dimensions of the field
width = 7
height = 10
field = initialise_field(width, height)

# displays the field line by line
for y in range(height):
    print(field[y])
