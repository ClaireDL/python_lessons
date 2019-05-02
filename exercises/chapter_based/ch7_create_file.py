#!/usr/bin/env python

import random

# create file with list of random length and of random integers
random_sample = [random.randint(-100, 100) for i in range(random.randint(0, 10))]
print(random_sample)

with open("sample.txt", "w+") as example_file:
    for element in random_sample:
        example_file.writelines("%s\n" % element)

# read from file and sums all the numbers, writing result to another file
sum = 0
with open("sample.txt", "r") as example_file:
    for element in example_file:
        print("%s" % element)
        sum += int(element)

with open("sum_result.txt", "w+") as result_file:
    result_file.write("%s" %sum)

# read from result_file
with open("sum_result.txt", "r") as result_file:
    print("the sum is: %s" % result_file.read())

#print("sum = %i" % sum)
