"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 22 Sep 2021
Homework Problem # 3_1
from 2 to 130, count odd numbers, even numbers,
squares of an int, cubes of an int
"""

import math

BEGIN = 2
END = 131  # include 130

odds_count = 0
evens_count = 0
squares_count = 0
cubes_count = 0

odds_list = []
evens_list = []
squares_list = []
cubes_list = []

print("Checking numbers from 2 to 130:")

for num in range(BEGIN, END):
    square_root = math.sqrt(num)
    # print odds w/ only start and end of range (like 1...129)
    if num % 2 != 0:
        odds_list.append(num)
        odds_count += 1
    # print evens w/ only start and end of range (like 2...130)
    if num % 2 == 0:
        evens_list.append(num)
        evens_count += 1
    # print list of squares
    if int(square_root + 0.5) ** 2 == num:
        squares_list.append(num)
        squares_count += 1
    # print list of cubes
    if round(num ** (1 / 3)) ** 3 == num:
        cubes_list.append(num)
        cubes_count += 1

print(f'Odd ({odds_count}) {odds_list[0]}...{odds_list[-1]}')
print(f'Even ({evens_count}) {evens_list[0]}...{evens_list[-1]}')
print(f'Square ({squares_count}): {squares_list}')
print(f'Cube ({cubes_count}): {cubes_list}')

# could refactor
# no need for the count vars, cound use len on each list
# should use END + 1 instead of adjusting the END constant
# should have used if-else for the even and odd

# could also have used filter(lambda()))