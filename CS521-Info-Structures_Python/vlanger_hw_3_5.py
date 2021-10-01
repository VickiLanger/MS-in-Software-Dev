"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 23 Sep 2021
Homework Problem # 3_5
read a file and print contents
"""

file = open("vlanger_hw_3/cs521_3_5_input.txt", "r")

lines = file.readlines()  # read the file cs521_3_5_input.txt, return list

line_tuples_list = list(enumerate(lines))  # Store each csv line as a tuple
print(line_tuples_list)

file.close()  # close the file


# could refactor
# instead of enumerate() which gives an unnecessary index
'''
student_list = []
for line in file:
    student_list.append(tuple([w.strip() for w in line.strip().split(",")]))
'''