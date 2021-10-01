"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 23 Sep 2021
Homework Problem # 3_4
file and error handling
"""
# NOTE: do NOT include txt files in zip folder
NUM_WORDS_PER_LINE = 5

try:
    file = open("vlanger_hw_3/cs521_3_4_input.txt", "r")
    text = file.read()
    words = text.split()  # get list of split strings
    # throw error if file != 20 words
    if len(words) == 20:
        output_file = open("vlanger_hw_3/cs521_3_4_output.txt", "w")

        # TODO: break sentence into 4 lines with 5 words each
        line_one = ' '.join(words[0:NUM_WORDS_PER_LINE])
        line_two = ' '.join(words[NUM_WORDS_PER_LINE:NUM_WORDS_PER_LINE*2])
        line_three = ' '.join(words[NUM_WORDS_PER_LINE*2:NUM_WORDS_PER_LINE*3])
        line_four = ' '.join(words[NUM_WORDS_PER_LINE*3:NUM_WORDS_PER_LINE*4])
        print(line_one, line_two)
        # write lines to cs521_3_4_output.txt
        output_file.write(line_one + '\n' +
                          line_two + '\n' +
                          line_three + '\n' +
                          line_four)
    else:
        print("File does not have 20 words. File has", len(words), "words")
except FileNotFoundError:
    print('file does not exist')  # print error if file is missing

file.close()


# could refactor

# assert?

# too much in the try block, do this instead, just for the stuff that can be messed up like user input and file names
# try:
#     file = open("vlanger_hw_3/cs521_3_4_input.txt", "r") then do except
# except FileNotFoundError:
#     print('file does not exist')

# try:
#     output_file = open("vlanger_hw_3/cs521_3_4_output.txt", "w")
# except IOError:
#     print('error')