"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 28 Sep 2021
Homework Problem # 4_2
use dictionary and find most frequent letter(s) in a string of 15 or more chars
"""

STRING = "I'm a green spotted kitty cat".upper()

# get rid of punctuation and whitespace characters
string_letters = "".join(c for c in STRING if c not in ("'",
                                                        " ",
                                                        "!",
                                                        ".",
                                                        "?",
                                                        ";",
                                                        '"',
                                                        "&"))

letter_count_dict = {}

letter_list = [char for char in string_letters]

# count number of each letter and save to dict {'I':1,}
for letter in letter_list:
    if letter in letter_count_dict:
        letter_count_dict[letter] += 1
    else:
        letter_count_dict[letter] = 1

# find letter(s) that repeats the most
keys_list = list(letter_count_dict.keys())
values_list = list(letter_count_dict.values())

max_repeated = []
max_repeat_count = max(values_list)
max_repeated_index = values_list.index(max_repeat_count)

# get all index positions with max repeat
indices = [i for i, val in enumerate(values_list) if val == max_repeat_count]

for i in indices:
    max_repeated.append(keys_list[i])

# print outputs
print(f'The string being analyzed is: "{STRING}"')
print("Dictionary of letter counts: {}".format(letter_count_dict))
# plural(s) for single letter vs. multiple frequent letters
if len(max_repeated) > 1:
    print(f"Most frequent letters {max_repeated} "
          f"appear {max_repeat_count} times")
else:
    print(f"Most frequent letter {max_repeated[0]} "
          f"appears {max_repeat_count} times")

# could refactor
# could have used if not .isalpha() continue
# 