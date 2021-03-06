#!/usr/bin/env python

from argparse import ArgumentParser
import argparse

parser = ArgumentParser()
parser.add_argument(
    '--people', '-p',
    default=1,
    type=int,
    help="The number of people"
)
parser.add_argument(
    '--flour', '-f',
    default=150,
    type=int,
    help="The quantity of flour in grams"
)
parser.add_argument(
    '--hydration', '-y',
    default=0.55,
    type=float,
    help="The hydration in baker's percentage"
)
parser.add_argument(
    '--fats', '-o',
    default=0.0,
    type=float,
    help="The amount of fats, in baker's percentage"
)
parser.add_argument(
    '--salt', '-s',
    default=0.02,
    type=float,
    help="The amount of salt, in baker's percentage"
)
parser.add_argument(
    '--sourdough', '-d',
    default=0.25,
    type=float,
    help="The amount of sourdough, in baker's percentage"
)
parser.add_argument(
    '--sourdough-hydration', '-a',
    default=0.5,
    type=float,
    help="The hydration of the sourdough"
)
parser.add_argument(
    '--portions', '-r',
    default=1,
    type=int,
    help="The number of portion to divide the dough in"
)
args = parser.parse_args()

# Calculates the quantity for each ingredient
flour_total = args.flour * args.people
sourdough = flour_total * args.sourdough
flour = flour_total / (1 + args.sourdough * (1.0 - args.sourdough_hydration))
water = flour_total * args.hydration - sourdough * args.sourdough_hydration
salt = flour_total * args.salt
# On effects of fats on hydration:
#   http://www.thefreshloaf.com/node/30743/where-does-oilhoney-and-sugar-fit-hydration-formulas
fats = flour_total * args.fats

# Total weight
total_weight = sourdough + water + flour + salt + fats

# Portioning
portion_weight = total_weight / float(args.portions)

# Estimate the rising time of the dough compared to the sourdough
rising_multiplier = args.sourdough_hydration / args.sourdough

# Display result
print("""
  ~  Baker's calculator  ~

Number of people: {0}

Selected quantities for one person:

  Total flour......: {1:.0f}g
  Hydration........: {2:.0f}%
  Sourdough........: {3:.0f}%
  SD hydration.....: {4:.0f}%
  Salt.............: {5:.0f}%
  Fats.............: {6:.0f}%

Total amounts for {0} person(s):

  Flour............: {7:.0f}g
  Water............: {8:.0f}g
  Sourdough........: {9:.0f}g
  Fats.............: {10:.0f}g
  Salt.............: {11:.1f}g

TOTAL WEIGHT: {12:.0f}g

Rising multiplier: {13:.2f}x""".format(
    args.people,
    args.flour,
    args.hydration * 100,
    args.sourdough * 100,
    args.sourdough_hydration * 100,
    args.salt * 100,
    args.fats * 100,
    round(flour),
    round(water),
    round(sourdough),
    round(fats),
    round(salt, 1),
    total_weight,
    round(rising_multiplier, 2)
))

if args.portions > 1:
    print("""
Portioning for {0} portions:

  Cut weight.......: {1:.0f}g""".format(
        args.portions,
        round(portion_weight)
    ))
