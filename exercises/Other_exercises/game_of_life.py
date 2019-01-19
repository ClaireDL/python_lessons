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

    def get_cell_status():
        """
        Gets the cell's next generation status on the basis of:
        - the present cell's status
        - the number of live neighbours
        """
        # a cell is alive is its value is 1, dead if its value is 0

        # counts the number of live neighbours
        counter_live_neighbours = 0
        for neighbour in neighbour_list:
            if neighbour == 1:
                counter_live_neighbours += 1

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

    for row in range(len(field)):
        for col in range(len(field[row])):
            index_neighbours = get_neighbours(row, col)
            print(index_neighbours)


# MAIN PROGRAM STARTS HERE
# Defines the dimensions of the field
width = 7
height = 10
field = initialise_field(width, height)

# displays the field as an array
#    for line in range(height):
#        print(field[line])
#    print()

#    print(iterate_through_field(field))

# testing iterate_through_field
test_field = [
    [0, 1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12, 13],
    [14, 15, 16, 17, 18, 19, 20]
]

#for test_line in test_field:
#    print(test_line)

iterate_through_field(test_field)
