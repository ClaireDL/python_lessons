#!/usr/bin/env python

import glob, os
import argparse
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    '--keyword', '-k',
    default=".py",
    type=str,
    help="The keyword in the files you want to retrieve"
)
parser.add_argument(
    '--path', '-p',
    default="C:/Users/chdell/Dropbox/Fabrizio&Claire/python_lessons",
    type=str,
    help="The path to the directory you are searching in"
)
args = parser.parse_args()

directory = os.chdir(args.path)

print("You are looking in %s" % args.path)
print("Files that contain %s: " % args.keyword)
for file in glob.glob("*%s*" % args.keyword):
    print(file)
