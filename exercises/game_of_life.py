#!/usr/bin/env python

import random

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

def get_neighbour_positions(xs):
    """
    Returns the position of a cell's neighbours as a list
    """
    neighbours = []
    global width
    global height


# Defines the dimensions of the grid
width = 7
height = 3
field = []

# Seed stage
# Creates nested lists for the field with random values of 0 or 1
for y in range(height):
    field.append([random.randint(0, 1) for i in range(width)])

for y in field:
    print(y)
