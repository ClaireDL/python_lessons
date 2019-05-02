#!/usr/bin/env python

import re

string = "This is a little text, so little it is extremely small. It is!"
print(string)

# removes punctuation
string = string.lower()
string_nopunctuation = re.sub(r"[\W]", " ", string)
string_nopunctuation = re.sub("  ", " ", string_nopunctuation)

# split string into a list of words, then sorts words
list_word = string_nopunctuation.split(" ")
list_word_sorted = sorted(list_word)
# removes the first element which is an empty string
list_word_sorted = list_word_sorted[1:]

word_counter = {}
for word in list_word_sorted:
    word_counter[word] = word_counter.get(word, 0) + 1
print(word_counter)
