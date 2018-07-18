#!/usr/bin/env python

import sys
import datetime

# write a program to print the current hour in words.
# 13:02 should be written "it is one o'clock", at 8:13 "it is quarter past 8". 9:52, "ten to ten"

hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute

# for each hour of the day, converts it into its word form "time"
# "timeplus" allows for expressions with the next hour word form.
if hour == 1 or hour == 13 :
    time = "one"
    timeplus = "two"
if hour == 2 or hour == 14 :
    time = "two"
    timeplus = "three"
if hour == 3 or hour == 15 :
    time = "three"
    timeplus = "four"
if hour == 4 or hour == 16 :
    time = "four"
    timeplus = "five"
if hour == 5 or hour == 17 :
    time = "five"
    timeplus = "six"
if hour == 6 or hour == 18 :
    time = "six"
    timeplus = "seven"
if hour == 7 or hour == 19 :
    time = "seven"
    timeplus = "eight"
if hour == 8 or hour == 20 :
    time = "eight"
    timeplus = "nine"
if hour == 9 or hour == 21 :
    time = "nine"
    timeplus = "ten"
if hour == 10 or hour == 22 :
    time = "ten"
    timeplus = "eleven"
if hour == 11 or hour == 23 :
    time = "eleven"
    timeplus = "twelve"
if hour == 12 :
    time = "twelve"
    timeplus = "one"

if 0 <= minute < 5 :
    if hour == 23 :
        print("It is midnight.")
    else :
        print("It is " + time + " O'clock.")
elif 5 <= minute < 12 :
    print("It is ten past " + time)
elif 12 <= minute < 17 :
    print("It is quarter past " + time)
elif 17 <= minute < 25 :
    print("It is twenty past " + time)
elif 25 <= minute < 35 :
    print("It is half past " + time)
elif 35 <= minute < 42 :
    print("It is forty past " + time)
elif 42 <= minute < 47 :
    print("It is quarter to " + timeplus)
elif 47 <= minute < 55 :
    print("It is ten to " + timeplus)
elif 55 <= minute <= 59 :
    if hour == 23 :
        print("It is midnight.")
    else:
        print("It is " + timeplus + " O'clock.")