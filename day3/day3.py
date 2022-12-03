''' https://adventofcode.com/2022/day/3 '''

import numbers
import string

# open the file and read it into a string
file    = "/home/ms/code/python/aoc2022/day3/input.txt"
f       = open(file, 'r')
file    = f.read()
file    = file.splitlines()

item_types  = list()
priorities  = list()

# Loop over each line
# split it in half
# store each half in a list for comparison
# check which item is in both compartments
# store the item in a list

for line in file:
    firsthalflist   = list()
    secondhalflist  = list()
    half = int(len(line)/2)
    firsthalflist   = (line[:half])
    secondhalflist  = (line[half:])
    # for the comparison, the values in a line must be made unique after the split
    firsthalflist = list(dict.fromkeys(firsthalflist))
    secondhalflist = list(dict.fromkeys(secondhalflist))
    for char in firsthalflist:
        if char in secondhalflist:
            item_types.append(char)

# Now we have all the item_types in a list
# calculate the values of the letters
# (ord("a") - 96)
# (ord("A") - 38)

for letter in item_types:
    if letter.isupper():
        priorities.append(ord(letter)-38)
    else:
        priorities.append(ord(letter)-96)

print(sum(priorities))

# 10684 - Too high, problem is too many item types 387 instead of 300
# 8243 - Right number

