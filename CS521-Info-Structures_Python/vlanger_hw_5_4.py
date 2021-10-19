"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 7 Oct 2021
Homework Problem # 5_4
return words the occur exactly twice in the given file
"""

while True:
    try:
        user_input = input("give a file name: ")
        break
    except FileNotFoundError:
        print("File does not exist, try again")


def remove_punctuation(file: str):
    '''remove punctuation from given file & return file without punctuation'''
    punctuation = """!@#$%^&*()_+-={}|[]\\:\";'<>?,./`~"""
    for char in file:
        if char in punctuation:
            file = file.replace(char, "")
    return file


with open(user_input, 'r') as file_data:
    data = file_data.read()
with open(user_input, "w+") as file_data:
    file_data.write(remove_punctuation(data))

file = open(user_input, "r")
file_as_list = file.readlines().split()  # read the file, return list
file.close()  # close file


def list_to_twice_words(file_lst: list):
    '''given a file, return words the occur exactly twice'''
    # check if indices were repeated twice and append to list
    repeated_twice_list = [i for i in set(file_lst) if file_lst.count(i) == 2]
    return repeated_twice_list


print("Words repeated exatly twice: ", list_to_twice_words(file_as_list))

#refactor
# could have used string module for string.punctuation()