#!/usr/bin/env python

def get_names(): return "asd"

#
# parsing arguments
#

import argparse
from argparse import ArgumentParser

# Setting up the argument parser
parser = ArgumentParser()
parser.add_argument(
    '--width', '-w',
    default=20,
    type=int,
    help="The width of the game field"
)
parser.add_argument(
    '--height', '-e',
    default=20,
    type=int,
    help="The height of the game field"
)
parser.add_argument(
    '--debug', '-d',
    action="store_true",
    help="Enables debug mode"
)
parser.add_argument(
    'field_file',
    nargs="?",
    help="The field file to load at startup"
)
args = parser.parse_args()

# How to reference the argument data
print("Requested width: %s" % args.width)
print("Requested height: %s" % args.height)
if args.debug:
    print("Debug mode enabled")
if args.field_file:
    print("Loading field file: %s" % args.field_file)

#
# list files with glob
#

import glob

# Listing all files
print("All files in the working directory: ")
print(glob.glob("*"))

# Listing using a wildcard
for python_file in glob.glob("*.py"):
    print("Python file: %s" % python_file)

#
# Import functions from a module
#

import beerlib

print(beerlib.get_names())
print(beerlib.get_adjectives())

from beerlib import get_random_name

print(
    get_random_name(
        beerlib.get_adjectives(),
        beerlib.get_names()
    )
)

#
# Importing packages
#

import beers.beerlib
beersbeerlib.beer_main()
