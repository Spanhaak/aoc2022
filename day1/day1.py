''' Advent of Code - Day one puzzle'''
'''This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?'''

# open the file and read it into a string
file    = "input.txt"
f       = open(file, 'r')
file    = f.read()

# do a splitlines to return the contents of each line for the for loop
file    = file.splitlines()

# set control values
value           = 0
highest_value   = 0

# loop over the content, with taken into account the newline evalutation and counting the non-newlines
# until it finds a newline, count the newly converted ints and set the highest value

for line in file:
    if line != '' :
        line = int(line)
        value = line + value
        if value > highest_value:
            highest_value = value
            print (value)
        else:
            continue    
    else:
        value = 0
