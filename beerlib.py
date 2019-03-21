#!/usr/bin/env python

import random

def get_names():
    return [
        "kriek", "hells", "ipa", "weisse", "porter"
    ]

def get_adjectives():
    return [
        "amazing", "awful", "weird", "fresh", "heavy"
    ]

def get_random_name(adjectives, names):
    return "%s_%s" % (
        adjectives[random.randrange(len(adjectives))],
        names[random.randrange(len(names))]
    )
