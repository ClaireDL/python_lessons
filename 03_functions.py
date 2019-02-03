#!/usr/bin/env python

# Just imports print_function from the package future
from __future__ import print_function


def multiply(number_a = 1, number_b = 1, number_c = 0.5):
    """
    This function multiplies three numbers as integers
    """
    return int(number_a * number_b * number_c * 2)

# Simple call
print(multiply(2, 3))
# Using default values
#  here the first argument receives 2, the other variables are default values
print(multiply(2))
# Passing an argument by name
# here first argument is 2, and assigns 3 to a specific argument, number_c
print(multiply(2, number_c=3))

print("This is a full line")
# Example of library function that uses named arguments
print("This is half a line", end="")
print(" and here the remaining")


def my_function_1(arg1, *list_args):
    """
    Function with variable arguments, as list
    """
    print("Argument #1: " + arg1)
    print(list_args)

my_function_1("This is arg1", "value2", 3, "value4")
print("arg1", "arg2", "arg3")


def my_function_1(arg1, **dict_args):
    """
    Function with variable arguments, as dictionary
    """
    print("Argument #1: " + arg1)
    print(dict_args)

my_function_1("This is arg1", arg2="value2", arg3=3, arg4="value4")


def outer():
    def inner():
        print("This is a print inside the inner function")

    inner()
    print("This is a print from the outer function")

outer()

def factorial(number):
    """
    Recursive function to calculate the factorial
    """
    if number == 1:
        return 1
    return factorial(number - 1) * number

print(factorial(5))

def factorial_tail(number, acc):
    """
    Recursive function to calculate the factorial
    """
    if number == 1:
        return acc
    return factorial_tail(number - 1, acc * number)

print(factorial_tail(5, 1))


def my_func_scope_1():
    var_1 = "B"
    print(var_1)

def my_func_scope_2():
    global var_1
    var_1 = "C"
    print(var_1)

var_1 = "A"
print(var_1)
my_func_scope_1()
print(var_1)
my_func_scope_2()
print(var_1)
