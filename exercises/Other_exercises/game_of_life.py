#!/usr/bin/env python

import random
import os

def game_of_life(col, row):
    """
    Runs the game of life until the system is stable,
    that is when two consecutive generations are identical
    """
    field = initialise_field(col, row)
    print_field(field)
    for counter in range(1000):
        next_generation = compute_next_generation(field)
        print_field(next_generation)
        field = next_generation
        os.system("clear")
    return print_field(next_generation)

def print_field(field):
    """
    Return the field as a two dimensional array
    """
    for line in range(len(field)):
        print(field[line])

def initialise_field(col, row):
    """
    Seed stage
    Initialises, e.g. populates, a field with a population of randomly selected alive
    (1) or dead (0) cells
    """
    return [[random.randint(0, 1) for i in range(col)] for y in range(row)]

def get_neighbours(field, row, col):
    """
    Returns the neighbours of a cell
    """
    neighbour_list = []
    # manage special cases for the next col and row
    # last col and row
    if row == len(field) - 1:
        next_row = 0
    else:
        next_row = row + 1
    if col == len(field[row]) - 1:
        next_col = 0
    else:
        next_col = col + 1

    neighbour_list.append(field[row - 1][col - 1])
    neighbour_list.append(field[row - 1][col])
    neighbour_list.append(field[row - 1][next_col])
    neighbour_list.append(field[row][col - 1])
    neighbour_list.append(field[row][next_col])
    neighbour_list.append(field[next_row][col - 1])
    neighbour_list.append(field[next_row][col])
    neighbour_list.append(field[next_row][next_col])

    return neighbour_list

def compute_next_generation(field):
    """
    Return the field with the next generation's cells' status
    """
    next_generation = []

    for row in range(len(field)):
        next_generation_by_row = []
        for col in range(len(field[row])):
            list_neighbours = get_neighbours(field, row, col)
            cell = field[row][col]
            #print(list_neighbours)
            cell_next_generation = get_cell_status(cell, list_neighbours)
            next_generation_by_row.append(cell_next_generation)
        next_generation.append(next_generation_by_row)

    return next_generation

def get_cell_status(cell, list_neighbours):
    """
    Gets the cell's next generation status on the basis of:
    - the present cell's status
    - the number of live neighbours
    """
    # a cell is alive is its value is 1, dead if its value is 0

    # counts the number of live neighbours
    counter_live_neighbours = 0
    for neighbour in list_neighbours:
        if neighbour == 1:
            counter_live_neighbours += 1
    #print(counter_live_neighbours)

    # parameters
    # live cell
    if cell == 1:
        # underpopulation
        if counter_live_neighbours < 2:
            cell = 0
        # survives
        elif 2 <= counter_live_neighbours <= 3:
            cell = 1
        # overpopulation
        elif counter_live_neighbours > 3:
            cell = 0

    # dead cell
    elif cell == 0 and counter_live_neighbours == 3:
        cell = 1

    return cell


# MAIN PROGRAM STARTS HERE
# Defines the dimensions of the field
col = 7
row = 10
game_of_life(row, col)

# testing compute_next_generation
test_field = [
   [0, 1, 2, 3, 4, 5, 6],
   [7, 8, 9, 10, 11, 12, 13],
   [14, 15, 16, 17, 18, 19, 20]
]
#print(compute_next_generation(test_field))

# testing get_cell_status
test_cell_status = [
    [1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0]
]
#print(test_cell_status)
#game_of_life = compute_next_generation(test_cell_status)
#print_field(game_of_life)
