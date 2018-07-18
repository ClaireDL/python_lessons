#!/usr/bin/env python

from __future__ import print_function

import csv
import numpy
import argparse


def distinct(input_list):
    """
    Eliminates duplicate from a list
    """
    return list(set(input_list))


def main():
    #
    # Step #1: We understand what the user want from the command line
    #

    # Read command line inputs and parameters
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input_file',
        default="results.csv",
        help='The path of the CSV input file.'
    )
    parser.add_argument(
        'input_file',
        default="results.csv",
        help='The path of the CSV output file.'
    )
    args = parser.parse_args()

    #
    # Step #2: We load all the file into a list
    #

    data = []

    # Open the current file for reading
    with open(args.input_file, "r") as input_file:
        # We scan all the lines of the file, one by one and
        for line in input_file.readlines():
            # We split each line in its constituent fields
            fields = line.strip().split(",")
            # Transform the data in the appropriate type and add it to the list
            data.append([
                fields[0], int(fields[1]), int(fields[2]), int(fields[3]) / 1000
            ])

    #
    # Step #3: Elaborate the data and write the output
    #

    #
    # Step #3.1: We understand what the columns and rows of the output file are
    #

    # List the sorting algorithms used and the sizes of the input lists
    sorting_algs = sorted(distinct(map(lambda x: x[0], data)))
    list_sizes = sorted(distinct(map(lambda x: x[1], data)))

    # Open the file that will contain the result
    with open("aggregate.csv", "w") as result_file:
        csv_writer = csv.writer(result_file)

        #
        # Step #3.2: Calculate the statistics for each algorithm/input_size and
        # we write the line in the output file
        #

        # Create and write the header of the CSV file
        columns = ["input_size"]
        for alg in sorting_algs:
            for stat in ["min", "max", "avg", "stddev", "percentile_90"]:
                columns.append("{0}_{1}".format(alg, stat))
        csv_writer.writerow(columns)

        # Scan through the sizes
        for size in list_sizes:
            # Initialize the row to write in the file
            row = [size]

            # Scan through the algorithms
            for alg in sorting_algs:
                # Extract from the relevant data points from the list
                data_points = filter(lambda x: x[0] == alg and x[1] == size, data)
                data_points = map(lambda x: x[3], data_points)

                # Calculate statistics on the execution time and add them to the
                # output row
                row.extend([
                    sum(data_points) / len(data_points),
                    min(data_points),
                    max(data_points),
                    numpy.std(data_points, ddof=1),
                    numpy.percentile(data_points, 90),
                ])

            # Write the row to the CSV file
            csv_writer.writerow(row)


if __name__ == '__main__':
    main()
