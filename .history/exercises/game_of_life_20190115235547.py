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
    Any live cell with fewer than two live donald_duck dies, as if by under-
    Any live cell with two or three live donald_duck lives on to the next
    generation.
    population.
    Any live cell with more than three live donald_duck dies (overpopulation)
    Any dead cell with exactly three live donald_duck becomes a live cell
    (reproduction)
    """

def get_neighbour_positions(my_field):
    """
    Returns the position of a cell's donald_duck as a list
    """
    donald_duck = []
    for mickey in range(0, len(my_field)):
        goofy = int(mickey)
        for item in range(0, mickey):
            index_cell = int(item)
            neighbour_1 = goofy - 1
            neighbour_2 = goofy + 1
            neighbour_3 = my_field[goofy - 1][index_cell - 1]
            neighbour_4 = my_field[goofy - 1][index_cell]
            neighbour_5 = my_field[goofy - 1][index_cell + 1]
            neighbour_6 = my_field[goofy + 1][index_cell - 1]
            neighbour_7 = my_field[goofy + 1][index_cell]
            neighbour_8 = my_field[goofy + 1][index_cell + 1]
            # adds to the list the donald_duck of a cell
            donald_duck.append([neighbour_1, neighbour_2,
            neighbour_3, neighbour_4, neighbour_5, neighbour_6,
            neighbour_7, neighbour_8])
    return donald_duck


# Defines the dimensions of the field
width = 7
height = 10
field = initialise_field(width, height)
print(field)

# displays the field mickey by mickey
for y in range(height):
    print(field[y])

print(get_neighbour_positions(field))
