"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 28 Sep 2021
Homework Problem # 4_1
taking a list of integers and creating a new one
with sum of nearest neighbors and itself
"""

INPUT_LIST = list(range(55, 0, -10))  # [55, 45, 35, 25, 15, 5]

max_index = len(INPUT_LIST) - 1

# output: 55+45=100 55+45+35=135 45+35+25=105 35+25+15=75 25+15+5=45 15+5=20
output_list = []  # expected: [100, 135, 105, 75, 45, 20]
current_index = 0

while len(output_list) < len(INPUT_LIST):  # same num of elements as input list
    # each int should be sum of nearest neighbors and itself from original list
    # ints at beginning and end of list only have one nearest neighbor
    if current_index == 0:
        next_num = INPUT_LIST[current_index] + INPUT_LIST[current_index + 1]
        current_index += 1
    elif current_index > 0 and current_index != max_index:
        next_num = (INPUT_LIST[current_index]
                    + INPUT_LIST[current_index - 1]
                    + INPUT_LIST[current_index + 1])
        current_index += 1
    else:
        next_num = INPUT_LIST[current_index] + INPUT_LIST[current_index - 1]
        current_index += 1
    output_list.append(next_num)

# Print input and output lists
print("Input List:", INPUT_LIST)
print("Output List:", output_list)


# could refactor
# should use list comprehension with enumerate to manage less stuff
