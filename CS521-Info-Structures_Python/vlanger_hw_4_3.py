"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 29 Sep 2021
Homework Problem # 4_3
zip lists together to make dictionary and fill in None
without using itertools.zip_longest()
"""

FIRST_NAMES = ['Aditi', 'Amun', 'Vicki']
LAST_NAMES = ['Lam', 'Langer', 'Liburd', "Morgan"]

# Validate that last name list is same size or > than first name list
if len(LAST_NAMES) == len(FIRST_NAMES) or len(LAST_NAMES) > len(FIRST_NAMES):
    print("Oops, more first names than last names.")
    if len(LAST_NAMES) > len(FIRST_NAMES):
        # more last names than first names? set missing first names to None
        difference = len(LAST_NAMES) - len(FIRST_NAMES)
        for i in range(0, difference):
            FIRST_NAMES.append(None)
    if len(LAST_NAMES) == len(FIRST_NAMES):
        # Use zip function to create a dict {'Last': 'First'}
        full_names_dict = dict(zip(LAST_NAMES, FIRST_NAMES))

# print input lists and zipped dict
print("First Names:", FIRST_NAMES)
print("Last Names:{}".format(LAST_NAMES))
print(f"Name Dictionary: {full_names_dict}")

# could refactor
# use assert to assume something is true, if not throw an error
# assert len(FIRST_NAMES) < (LAST_NAMES), ('Error: first names > last names')
