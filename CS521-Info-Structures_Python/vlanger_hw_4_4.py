"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 29 Sep 2021
Homework Problem # 4_4
play with dictionary by keys and values
"""

my_dict = {'a': 15, 'c': 18, 'b': 20}

# keys as list
keys_list = list(my_dict.keys())
print(f'Keys: {keys_list}')

# comma separated values
values_list = list(my_dict.values())
stringified_values_list = [str(i) for i in values_list]
values_str = ", ".join(stringified_values_list)
print(f'Values: {values_str}')

# key-value pairs as formatted data
key_value_pairs = ', '.join('{}: {}'.
                            format(k, int(v)) for k, v in my_dict.items())
print(f'Key value pairs: {key_value_pairs}')

# sort in ascending order by key and print list of tuples for key-value pairs
keys_sorted_list = sorted(list(my_dict.items()))
print(f'Key value pairs ordered by key: {keys_sorted_list}')

# sort in ascending order by value and print all key-value pairs
values_sorted_list = sorted([(value, key) for (key, value) in my_dict.items()])
print("Key value pairs ordered by value:")
for k, v in values_sorted_list:
    print(f'{v}: {k}', end=", ")

# could refactor
# operator.itemgetter()
