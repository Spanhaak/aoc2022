''' https://adventofcode.com/2022/day/4 '''

from genericpath import exists

# open the file and read it into a list
file    = "/home/ms/code/python/aoc2022/day4/input.txt"
f       = open(file, 'r')
file    = f.read()
file    = file.splitlines()

count = 0
overlap = list()
overlapping = list()

# Loop through the items
for line in file:
    
    result_one = list()

    # Split the assignments for comparison
    first_section = line.split(',')
    first_section = first_section[0]

    a, b = first_section.split('-')
    a, b = int(a), int(b)

    result_one = range(a, b + 1)
    first_set = list(result_one)

    # Check the second part

    result_two = list()

    second_section = line.split(',')
    second_section = second_section[1]
   
    a, b = second_section.split('-')
    a, b = int(a), int(b)

    result_two = range(a, b + 1)
    second_set = list(result_two)

    # Validate the overlap between the sets
    
    if first_section == second_section:
        count=count+1

    overlap.append(all(e in second_set for e in first_set))
    overlap.append(all(e in first_set for e in second_set))


everything = (sum(overlap))
print(everything - count)

# 444 is my answer

