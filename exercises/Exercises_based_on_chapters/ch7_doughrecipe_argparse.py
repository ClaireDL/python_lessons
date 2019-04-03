#!/usr/bin/env python

import argparse
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    '--flour', '-f',
    default=150,
    type=int,
    help="The quantity of flour"
)
parser.add_argument(
    '--hydration', '-hyd',
    default=52,
    type=int,
    help="The hydration in percentage"
)
parser.add_argument(
    '--people', '-p',
    default=2,
    type=int,
    help="The number of people"
)
parser.add_argument(
    '--oil', '-o',
    default=1,
    type=int,
    help="The percentage of oil"
)
args = parser.parse_args()

# Calculates the quantity for each ingredient
flour_total = args.flour * args.people
sourdough = float(flour_total / 4)
water = float(args.hydration * flour_total / 100 - sourdough/2)


if args.people == 1:
    print("Recipe for 1 person with {0} hydration:".format(args.hydration))
else:
    print("Recipe for {0} people with {1:.0f} hydration:".format(args.people, args.hydration))
print("{0:.0f}g of flour".format(flour_total))
print("{0:.0f}g of water".format(water))
print("{0:.0f}g of sourdough".format(sourdough))
