"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 29 Sep 2021
Homework Problem # 4_5
convert numbers to text using dict with nums as keys and words as values
"""

NUMBERS_DICT = {'1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
                '0': 'zero',
                '-': 'negative',
                '.': 'point'}

# use infinite loop and validate input. break if valid
while True:
    try:
        user_input = float(input("Give a number: "))
        break
    except ValueError:
        print('Oops, that wasn\'t a valid number')

user_input_str = str(user_input)
max_index = len(user_input_str) - 1

num_as_word_list = []
# convert the validated user_input to words using numbers_dict
current_index = 0

while current_index <= max_index:
    for key, value in NUMBERS_DICT.items():
        if current_index <= max_index:
            if user_input_str[current_index] in key:
                current_index += 1
                num_as_word_list.append(value)


num_as_word = " ".join(num_as_word_list)
# print the converted number words
print(f"Your number as text: {num_as_word}")

# could refactor
# if ',' in user_input:
#       print("try again without commas")
# a lot less code to use a for loop than whatever mess I did above
# for digit in user_input:
#       print(NUMBERS_DICT[digit], end=" ")
