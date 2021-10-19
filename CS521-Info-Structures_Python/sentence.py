"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 13 Oct 2021
Homework Problem # 6
use a class & methods to evaluate and manipulate a sentence
"""

import string
import random


class Sentence():
    '''a class to represent a sentence'''

    exclude = string.punctuation

    def __init__(self, sentence=""):
        '''initialize constructor'''
        self.sentence_str = sentence
        self.alpha_sentence_str = "".join(char for char in self.sentence_str
                                          if char not in self.exclude)

    def get_all_words(self):
        '''given no args return sentence as a list'''
        self.sentence_list = list(self.alpha_sentence_str.split())
        return self.sentence_list

    def get_word(self, desired_word_index):
        '''given index position, get desired word from sentence'''
        desired_word = self.sentence_list[desired_word_index]
        return desired_word

    def set_word(self, index, new_word):
        '''given index position and new word, set desired word from sentence'''
        subbed_word = self.sentence_list[index] = new_word
        return subbed_word

    def scramble(self):
        '''given no args, return scrambled list of all words in a sentence'''
        list = self.sentence_list
        scrambled_list = random.sample(list, len(list))
        return scrambled_list

    def __repr__(self):
        '''print original instance string with a period at the end'''
        instance = self.sentence_str
        if "." not in instance:
            instance += "."
        return instance


if __name__:
    words_str = Sentence("I'm a green spotted kitty cat with purple paws.")
    words_list = words_str.get_all_words()
    original_words_str = " ".join(words_list)
    word = words_str.get_word(3)
    sub_word = words_str.set_word(3, "slimy")
    initial_str_copy = "".join(original_words_str)
    scrambled_words = words_str.scramble()
    assert set(scrambled_words) != set(repr(words_str)), ('Error: set_word() \
                                                     did not work')
    print("Sentence.py - unit test successful")
    print("original: " + repr(words_str))
    print("scrambled: " + " ".join(scrambled_words))
    print("final version: " + " ".join(words_list))
