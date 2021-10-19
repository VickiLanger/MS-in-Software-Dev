"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 6 Oct 2021
Homework Problem # 5_1
count vowels & consonants in a file using functions and error handling
"""

# repeatedly prompt for file until correct
while True:
    try:
        user_input = input('Give a text file name (example: "cats.txt"): ')
        break
    except FileNotFoundError as error:
        print("Error: ", error)


def vc_counter(user_file: str):
    '''count vowels and consonants from a file'''
    # open file and readlines
    file = open(user_input, "r")
    file_list = file.readlines().split()  # read the file, return list
    file.close()  # close file
    file_string = ""
    for word in file_list:
        file_string += word
    letter_count_dict = {}
    vowel_count = 0
    consonant_count = 0
    for char in file_string.upper():
        # without counting non-alpha characters
        if char in "AEIOU":  # count vowels
            vowel_count += 1
        if char in "BCDFGHJKLMNPQRSTVWXYZ":  # count consonants
            consonant_count += 1
    # add dict key-value pairs
    letter_count_dict['vowels'] = vowel_count
    letter_count_dict['consonants'] = consonant_count
    return letter_count_dict  # {'vowels': 34, 'consonants': 12}


letter_counts = vc_counter(user_input)

# outputs
print("Total # of vowels in your file: ", letter_counts['vowels'])
print("Total # of consonants in your file: ", letter_counts['consonants'])

# could refactor
# instead of try-except, could do this
#if os.path.exists(file)
#    break
#
# file_string = ' '.join(file.readlines())
