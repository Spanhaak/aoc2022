''' https://adventofcode.com/2022/day/5 '''

from itertools import islice

with open("input.txt", 'r', encoding = 'utf-8') as f:
    # give me the first 8 rows
    head = [next(f) for x in range(8)]

    # Get the letters of the stacks in a list
    list_of_values = (1, 5, 9, 13, 17, 21, 25, 29, 33)

    for value in list_of_values:
        temp_list=[]
        for line in head:
            entry=(line[value])
            if entry == '' or entry == ' ':
                continue
            temp_list.append(entry)
        if value == 1 : list1 = value = temp_list[::-1]
        if value == 5 : list2 = value = temp_list[::-1]
        if value == 9 : list3 = value = temp_list[::-1]
        if value == 13 : list4 = value = temp_list[::-1]
        if value == 17 : list5 = value = temp_list[::-1]
        if value == 21 : list6 = value = temp_list[::-1]
        if value == 25 : list7 = value = temp_list[::-1]
        if value == 29 : list8 = value = temp_list[::-1]
        if value == 33 : list9 = value = temp_list[::-1]

    # List have been created
    # Give me the rest of the file
    # Provide actions needed
    #body = [next(f) for x in range(503)]
    body = [next(f) for x in range(3)]
    for line in body:
        if line.startswith('move'):
            print(line)
            print(value)


# WIP continue later
