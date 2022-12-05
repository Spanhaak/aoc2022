''' https://adventofcode.com/2022/day/5 '''

from itertools import islice

# First generate a list of stacks
list_of_values = []

with open("input.txt", 'r', encoding = 'utf-8') as f:
    values_line = [next(f) for x in range(9)]
    values_line = values_line[-1]
    for number in values_line:
        if number == " " or number == '':
            continue
        else:
            list_of_values.append(values_line.rfind(number))
    
# Create lists for holding the boxes
with open("input.txt", 'r', encoding = 'utf-8') as f:
    head = [next(f) for x in range(8)]

    bunch_of_crates = {}
    
    for value in list_of_values:
        temp_list=[]
        for line in head:
            entry=(line[value])
            if entry == '' or entry == ' ':
                continue
            temp_list.append(entry)
        if value == 1 : bunch_of_crates['1']=list1 = value = temp_list[::-1]
        if value == 5 : bunch_of_crates['2']=list2 = value = temp_list[::-1] 
        if value == 9 : bunch_of_crates['3']=list3 = value = temp_list[::-1]
        if value == 13 : bunch_of_crates['4']=list4 = value = temp_list[::-1]
        if value == 17 : bunch_of_crates['5']=list5 = value = temp_list[::-1]
        if value == 21 : bunch_of_crates['6']=list6 = value = temp_list[::-1]
        if value == 25 : bunch_of_crates['7']=list7 = value = temp_list[::-1]
        if value == 29 : bunch_of_crates['8']=list8 = value = temp_list[::-1]
        if value == 33 : bunch_of_crates['9']=list9 = value = temp_list[::-1]

    body = [next(f) for x in range(503)]

    for line in body:
        if line.startswith('move'):
            line = line.replace('from ', '')
            line = line.replace('to ', '')
            line = line.replace('move ', '')
            line = line.split(" ")
            
            from_dict   = line[1]
            from_dict   = from_dict.rstrip()
            to_dict     = line[2]
            to_dict     = to_dict.rstrip()
            boxes       = int(line[0])
            print(boxes)
        
            selected_crates = (bunch_of_crates[from_dict][-boxes:])
            for each_box in selected_crates: (bunch_of_crates[to_dict].append(each_box))
            for each_box in selected_crates: (bunch_of_crates[from_dict].remove(each_box))   


    final = (bunch_of_crates['1'][0], bunch_of_crates['2'][0], bunch_of_crates['3'][0], bunch_of_crates['4'][0], bunch_of_crates['5'][0], bunch_of_crates['6'][0], bunch_of_crates['7'][0], bunch_of_crates['8'][0], bunch_of_crates['9'][0])
    final = (' '.join(final))
    final = final.replace(" ", '')
    print(final)
    # BWQZJNRLF   