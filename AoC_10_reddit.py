# https://github.com/viliampucik/adventofcode/blob/master/2020/10.py

import fileinput
from collections import defaultdict

addapters = [0] + sorted(map(int, fileinput.input('day_10.txt')))
print(addapters, '\n\n')
addapters.append(addapters[-1] + 3)
print(addapters, '\n\n')

diffs = defaultdict(int)
print(diffs, '\n\n')
counts = defaultdict(int, {0: 1})
print(counts, '\n\n')

for a, b in zip(addapters[1:], addapters):
    diffs[a - b] += 1
    # number of ways to reach i'th adapter from previous three possible ones
    counts[a] = counts[a - 3] + counts[a - 2] + counts[a - 1]

print(diffs[1] * diffs[3])
print(counts[addapters[-1]])