"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 22 Sep 2021
Homework Problem # 3_2
Use a loop to count uppercase, lowercase, digits, and punctuation.
Then output in neat rows using str formatting
"""

import string

SENTENCES = ("I have 2 cats, 2 dogs, & a fish named Chip.",
             "I've been coding since 2018.",
             "I'll get a 100 on this project.")

row = 0

# give headings and underline
print("{:^3}{:^7} {:^8} {:^8} {:^8}".
      format("#", "# Upper", "# lower", "# Digits", "# Punct."))
print("{:^3}{:^7} {:^8} {:^8} {:^8}".
      format("-", "-------", "--------", "--------", "--------"))


for sentence in SENTENCES:
    row += 1
    uppercase = 0
    lowercase = 0
    digits = 0
    punctuation = 0
    for char in sentence:
        # count the uppercase
        if char >= 'A' and char <= 'Z':
            uppercase += 1
        # count the lowercase
        elif char >= 'a' and char <= 'z':
            lowercase += 1
        # count the digits
        elif char.isnumeric():
            digits += 1
        # count the punctuation
        elif char in string.punctuation:
            punctuation += 1
    print("{:^3}{:^7} {:^8} {:^8} {:^8}".
          format(row, uppercase, lowercase, digits, punctuation))

# could refactor

# could use islower() isupper() isdigit() string.punctuation
#like: uppercase += char.isupper()

# could do better on underline
# print({d:-^3s}{d:-^7s} {d:-^8s} {d:-^8s} {d:-^8s}".format(d="-"))