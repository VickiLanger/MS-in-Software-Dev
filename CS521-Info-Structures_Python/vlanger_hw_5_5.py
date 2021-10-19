"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 7 Oct 2021
Homework Problem # 5_5
recursion in a function using factorials
"""

while True:
    try:
        user_input = int(input("Give a factorial starting integer: "))
        break  # end when no error is thrown
    except ValueError as error:
        print(error, "Please try again")


def factorial(num: int):
    '''given user int, calculate & return factorial using recursion'''
    if num == 0 or num == 1:  # define base case
        return 1
    else:
        return num * factorial(num-1)


def factorial2(num: int):
    '''given user int, calculate & return factorial without using recursion'''
    result = 1  # start at 1
    for i in range(1, num+1):
        result = result * i
    return result


# print formatted with thousand commas
print("Factorial with recursion ", factorial(user_input))
print("Factorial without recursion ", factorial2(user_input))
