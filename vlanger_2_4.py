"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 14 Sep 2021
Homework Problem # 2_4
even or odd without an if statement in 3 commands
"""

user_input = input("Give a number: ")  # ask user for num
num = int(user_input)  # cast to int
print(f"{num} is odd" * (num % 2 != 0), f"{num} is even" * (num % 2 == 0))
