#!/usr/bin/env python

test = [{
    'name': 'Fabrizio',
    'age': 32
}, {
    'name': 'Adam',
    'age': 13
}]

# Filter
print(filter(lambda x: x['age'] > 20, test))
# List comprehension
print([x for x in test if x['age'] > 20])
# Iteration
result = []
for x in test:
    if x['age'] > 20:
        result.append(x)
print(result)

# Reduce
print(reduce(lambda x, y: y['age'] + x['age'], test) / float(len(test)))
# Map-Sum
print(sum(map(lambda x: x['age'], test)) / float(len(test)))
# Iteration
average, size = 0.0, 0
for x in test:
    average += x['age']
    size += 1
average /= size
print(average)
