#!/usr/bin/env python

from __future__ import print_function

import os
import time
import random
import sorting
import argparse


def test_algorithm(sort_function, csv_file, max_size, steps, count):
    """
    This function performs performance tests on a given sorting algorithm
    """

    #
    # Step #2.1: We take care of the file that will hold the results
    #

    # Remove existing file
    if os.path.exists(csv_file):
        os.remove(csv_file)

    # We open here the CSV file to write on it the result of the tests
    with open(csv_file, "a") as csv_file:

        #
        # Step #2.2: We go through all test cases, in this case the sizes on the
        # inputs how many time we perform the test for each input size.
        #

        for list_size in range(0, max_size, int(max_size / steps)):
            # This is the list to sort that contains random numbers
            test_list = [random.random() for i in range(list_size)]

            print("    Testing with #{0} items: ".format(list_size), end='')
            for try_count in range(count):
                #
                # Step #2.3: We perform the test and count the execution time
                #

                # Get the function from its name
                sort_algorithm = eval(sort_function)

                # Run the sorting algorithm
                start_time = time.time()
                result = sort_algorithm(test_list)
                stop_time = time.time()

                # Calculate the execution time in microseconds
                exec_time = int(round((stop_time - start_time) * 1E+6))
                print("{0}ms ".format(exec_time / 1000), end='')

                #
                # Step #2.4: We write the output in the file
                #

                # Write result in the file
                csv_file.write("{0},{1},{2},{3}\n".format(
                    sort_function, len(test_list), try_count, exec_time
                ))

            print("")


def main():
    #
    # Step #1: We understand what the user want from the command line
    #

    # Read command line inputs and parameters
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--count',
        type=int,
        default=5,
        help='How many test to perform on a given input size.'
    )
    parser.add_argument(
        '--size',
        type=int,
        default=5000,
        help='Maximum size of the input.'
    )
    parser.add_argument(
        '--steps',
        type=int,
        default=50,
        help='How many size steps to perform.'
    )
    parser.add_argument(
        'output_file',
        help='The path of the CSV output file.'
    )
    args = parser.parse_args()

    #
    # Step #2: We perform the tests
    #

    # Perform the tests
    print("Test started")

    print("  Running test on INSERTION sort")
    test_algorithm("sorting.insertion", args.output_file, args.size, args.steps, args.count)

    print("  Running test on MERGE sort")
    test_algorithm("sorting.merge", args.output_file, args.size, args.steps, args.count)


#
# Starting point
#
if __name__ == '__main__':
    main()
