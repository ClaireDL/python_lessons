#!/usr/bin/env python
#
# Given a list of strings calculate the average word length
#

my_list = [
    "Given", "a", "list", "of", "strings", "calculate", "the", "average",
    "word", "length"
]


# NEVER EVER TO SEE INDEX AGAIN
list_length = []
for i in range(0, len(my_list)):
    list_length.append(len(my_list[i]))
result = float(sum(list_length)) / float(len(list_length))
print(result)


# Proper Python way, cleaner and faster
total_characters = 0
total_words = 0.0
for word in my_list:
    total_characters += len(word)
    total_words += 1.0
result = total_characters / total_words
print(result)

# Using map
result = sum(map(lambda x: len(x), my_list)) / float(len(my_list))
print(result)

# Using list comprehension
#word_lengths = [len(word) for word in my_list]
#average_length = sum(word_lengths) / float(len(my_list))
result = sum([len(word) for word in my_list]) / float(len(my_list))
print(result)
