"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 6 Oct 2021
Homework Problem # 5_2
refactor of hw_4_2; use funcs to get most frequent letters & provide histogram
"""


def letter_counts(sentence: str):
    '''take a string and return frequency of characters'''
    # remove punctuation and spaces
    punctuation = """ !@#$%^&*()_+-={}|[]\\:\";'<>?,./`~"""
    for char in sentence:
        if char in punctuation:
            sentence = sentence.replace(char, "")
    # count alpha characters
    letter_count_dict = {}
    for char in sentence.upper():
        if char in letter_count_dict:
            letter_count_dict[char] += 1
        else:
            letter_count_dict[char] = 1
    # return dict of keys and frequency of each letter
    return letter_count_dict


def most_common_letter(sentence: str):
    '''take a string and return most common letters as list'''
    letter_count_dict = letter_counts(sentence)
    # find letter(s) that repeats the most
    keys_list = list(letter_count_dict.keys())
    values_lst = list(letter_count_dict.values())

    max_repeated = []
    max_repeat_cnt = max(values_lst)
    # max_repeated_index = values_list.index(max_repeat_count)

    # get all index positions with max repeat
    indices = [i for i, val in enumerate(values_lst) if val == max_repeat_cnt]

    for i in indices:
        max_repeated.append(keys_list[i])
    most_common_letter_list = []
    # print outputs
    # print("Dictionary of letter counts: {}".format(letter_count_dict))
    # plural(s) for single letter vs. multiple frequent letters
    if len(max_repeated) > 1:
        return f"Most common letters {max_repeated} 🔁 {max_repeat_cnt} times"
    else:
        return f"Most common letter {max_repeated[0]} 🔁 {max_repeat_cnt} times"
    # call letter_counts()
    # return list of the most common letters
    return most_common_letter_list


def string_count_histogram(sentence: str):
    '''take a string and return histogram of characters'''
    letter_count_dict = letter_counts(sentence)
    histogram_list = []
    for key, value in letter_count_dict.items():
        histogram_list.append(key*value)
    histogram_list.sort()
    return histogram_list


if __name__ == '__main__':
    string = "I'm a green spotted kitty cat with purple paws."
    data_dict = letter_counts(string)
    letter_count_str = "".join("'{}':{}, ".
                               format(k, v) for k, v in data_dict.items())
    print("fequency of each letter: ", letter_count_str)
    print(most_common_letter(string))
    for index in string_count_histogram(string):
        print(index)
