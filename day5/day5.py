""" https://adventofcode.com/2022/day/5 """

# First generate stacks
list_of_values = []

with open("input.txt", "r", encoding="utf-8") as f:
    values_line = [next(f) for x in range(9)]
    values_line = values_line[-1]
    for number in values_line:
        if number == " " or number == "":
            continue
        else:
            list_of_values.append(values_line.rfind(number))

# Create lists for holding the boxes
with open("input.txt", "r", encoding="utf-8") as f:
    head = [next(f) for x in range(8)]
    bunch_of_crates = {}

    for i, value in enumerate(list_of_values):
        temp_list = []
        for line in head:
            entry = line[value]
            if entry == "" or entry == " ":
                continue
            temp_list.append(entry)

        bunch_of_crates[str(i + 1)] = temp_list[::-1]

    body = f.readlines()[2:]

    for line in body:
        line = line.replace("from ", "")
        line = line.replace("to ", "")
        line = line.replace("move ", "")
        line = line.split(" ")

        from_dict = line[1]
        from_dict = from_dict.rstrip()
        to_dict = line[2]
        to_dict = to_dict.rstrip()
        boxes = int(line[0])

        selected_crates = bunch_of_crates[from_dict][-boxes:]
        for each_box in reversed(selected_crates):
            bunch_of_crates[to_dict].append(each_box)
            bunch_of_crates[from_dict].pop()

    final = "".join(v[-1] for v in bunch_of_crates.values())
    print(final)

    # HNFFVRLCJ