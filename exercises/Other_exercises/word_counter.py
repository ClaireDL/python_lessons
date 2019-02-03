#!/usr/bin/env python

import re

string = "This is a little text, so little it is extremely small. It is!"

# removes punctuation
string = string.lower()
string_nopunctuation = re.sub(r"[\W]", " ", string)
string_nopunctuation = re.sub("  ", " ", string_nopunctuation)

# split string into a list of words, then sorts words
list_word = string_nopunctuation.split(" ")
list_word_sorted = sorted(list_word)
# removes the first element which is empty
list_word_sorted = list_word_sorted[1:]

counter = {}
for word in list_word_sorted:
    counter[word] = counter.get(word, -1) + 1
print(counter)
