''' https://adventofcode.com/2022/day/3 '''

from genericpath import exists
import numbers
import string

# open the file and read it into a list
file    = "/home/ms/code/python/aoc2022/day3/input.txt"
f       = open(file, 'r')
f       = [line[:-1] for line in f]

print(len(f))
# 300

group_letters   = []
priorities      = []

# Loop over the contents of the file per three entries
# store those entries in a list for comparison
for a, b, c in zip(*[iter(f)]*3):
    threesoms = list()
    threesoms = (a, b, c)
    print(threesoms)
    # the fucking list must contain uniques otherwise double counting occurs
    for each_letter in set(threesoms[0]):
        if each_letter in threesoms[1] and each_letter in threesoms[2]:
            group_letters.append(each_letter)
        else:
            continue

print (group_letters)

print (len(group_letters))
# needs to be 100, but is 121 in first try

# Now we have all the item_types in a list
# calculate the values of the letters
# (ord("a") - 96)
# (ord("A") - 38)

for letter in group_letters:
    if letter.isupper():
        priorities.append(ord(letter)-38)
    else:
        priorities.append(ord(letter)-96)

print(sum(priorities))