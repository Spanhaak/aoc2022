''' https://adventofcode.com/2022/day/2 '''

# A - Rock      
# B - Paper
# C - Scissors

# Y - Paper
# X - Rock
# Z - Scissors

# 1 - Rock
# 2 - Paper
# 3 - Scissors

''' The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

'''

''' Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.'''


# open the file and read it into a string
file    = "input.txt"
f       = open(file, 'r')
file    = f.read()

# do a splitlines to return the contents of each line for the for loop
file    = file.splitlines()

# set control values
points          = 0
highest_points  = 0


for line in file:
    if line[0] == 'A' and line[2] == 'Y':
        points = 8
        highest_points = highest_points + points
    if line[0] == 'A' and line[2] == 'X':
        points = 4
        highest_points = highest_points + points
    if line[0] == 'A' and line[2] == 'Z':
        points = 3 
        highest_points = highest_points + points
    if line[0] == 'B' and line[2] == 'Y':
        points = 5
        highest_points = highest_points + points
    if line[0] == 'B' and line[2] == 'X':
        points = 1
        highest_points = highest_points + points
    if line[0] == 'B' and line[2] == 'Z':
        points = 9 
        highest_points = highest_points + points
    if line[0] == 'C' and line[2] == 'Y':
        points = 2
        highest_points = highest_points + points
    if line[0] == 'C' and line[2] == 'X':
        points = 7
        highest_points = highest_points + points
    if line[0] == 'C' and line[2] == 'Z':
        points = 6
        highest_points = highest_points + points
    
    print (highest_points)

## Part II of day 2

# Y = Draw
# X = Lose
# Z = Win

# A - Rock      
# B - Paper
# C - Scissors
