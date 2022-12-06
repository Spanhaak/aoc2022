'''https://adventofcode.com/2022/day/6'''

with open("/Users/marco.spanhaak1/code/python/aoc2022/day6/input.txt", "r", encoding="utf-8") as f:
    data = f.read()

# example: mjqjpqmgbljsphdztnvjfqwrcgsmlb
# jpqm
# after 7th char

# Some characteristics on the input

first_bit   = 0
second_bit  = 4
last_bit    = len(data)
control_bit = 0

# first check the first 4 characters and evaluate if it is a marker
def check_unique(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i] == str[j]):
                return False
    return True

list_of_matches = []

while control_bit <= last_bit:
    selection = data[first_bit:second_bit]
    first_bit = first_bit + 1
    second_bit = second_bit + 1
    control_bit = control_bit + 1
    
    if (check_unique(selection)):
        print(selection)
        list_of_matches.append(selection)
    else:
        print("not")

print(list_of_matches)

first_slice = data.partition(list_of_matches[0])
len_slice = (len(first_slice[0]))
print(len_slice + 4) 