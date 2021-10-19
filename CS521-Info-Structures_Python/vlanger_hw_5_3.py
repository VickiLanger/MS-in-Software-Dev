"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 6 Oct 2021
Homework Problem # 5_3
playing with error handling
"""

while True:
    try:
        user_input = input("Give 4 numbers separated by a space: ")
        # break apart the numbers given into different vars
        num_one, num_two, num_three, num_four = user_input.split()
        # first num * second num, then + third num, finally, / fourth num
        result = ((int(num_one) * int(num_two)) +int(num_three)) /int(num_four)
        break  # end when no error is thrown
    except ZeroDivisionError as error:
        print(error, "cannot divide by zero")
    except ValueError as error:
        print(error)
    except IndexError as error:
        print(error)

# print equation and result
print(f'(({num_one} * {num_two}) + {num_three}) / {num_four} = {result}')

# should refactor
# user input should've had it's very own try block