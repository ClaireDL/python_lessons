#!/usr/bin/env python

import numpy


def display_grid(x, y, xs):
    """
    Displays a formatted grid to represent the environment
    """
    first_element = 0
    for element in range(0, y):
        last_element = first_element + x
        line = xs[first_element:last_element]
        print(line)
        first_element = last_element

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

def get_neighbour_positions(x, y, index):
    """
    Returns the position of a cell's neighbours as a list
    """
    neighbours = []

    def get_previous_line():
        if index == 0 :
            return [x * y - 1, (y - 1) * x, (y - 1) * x + 1]
        if 1 <= index < x:
            return [(y - 1) * x + index, (y - 1) * x + index - 1, (y - 1) * x + index + 1]
        return [index - x - 1, index - x, index - x +1]

    def get_same_line():
        if index == 0:
            return [x - 1, 1]
        if index == x * y:
            return [index - 1, (y - 1) * x]
        return [index - 1, index + 1]

    def get_next_line():
        if index == 0:
            return [(2 * x) - 1, x, x + 1]
        if index == x * y:
            return [x - 2, x - 1, 0]
        if ((y - 1) * x) <= index < (y * x):
            return [index - (y - 1) * x]
        return [index + x - 1, index + x , index + x + 1]

    neighbours.extend(get_previous_line())
    neighbours.extend(get_same_line())
    neighbours.extend(get_next_line())
    return neighbours

# Defines the dimensions of the grid
width = 7
height = 3

# Seed stage
# Creates a list for the grid with random values of 0 or 1
seed = [numpy.random.randint(2) for i in range(height * width)]

# displays the seed in a formatted grid
display_grid(width, height, seed)

