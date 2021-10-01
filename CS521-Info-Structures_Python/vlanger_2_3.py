"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 14 Sep 2021
Homework Problem # 2_3
format function and f-strings
"""

num = int(input("Give an integer: "))  # ask user for num
result = num+num/3+num*num*num+num*num**3  # do math
result_with_decimal = float("{:.2f}".format(result))  # 2 decimal w/ str format
final_result = "{:,}".format(result_with_decimal)  # add comma seperator
print(f'''{num}+{num}/3+{num}*{num}*{num}+{num}*{num}**3
      = {final_result}''')  # print formula & result
