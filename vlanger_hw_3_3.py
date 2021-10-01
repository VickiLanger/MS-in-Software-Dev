"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 23 Sep 2021
Homework Problem # 3_3
prompt user for 3-digit num with ascending non duplicate digits (like 123, 259)
throw errors if not int or not ascending
"""

try:

    number_not_obtained = True
    while True:
        user_str = input("enter a 3-digit integer")  # ask for 3 digit int
        user_int = int(user_str)
        first_digit = user_str[:1]
        second_digit = user_str[1:2]
        third_digit = user_str[2:3]
        # check that digits are in ascending order
        if first_digit < second_digit and second_digit < third_digit:
            # check there are ONLY 3 digits
            if user_int < 1000 and user_int > 99:
                # check for duplicate digits
                if (first_digit != second_digit or
                    second_digit != third_digit or
                    third_digit != first_digit):
                    print("Success: number accepted!")  # success
                    break  # number_not_obtained = False
                else:
                    print("Error: Please do not use duplicate digits")  # fail
            else:
                print("Error: Please use a 3-digit whole number")  # fail
        else:
            print("Error: The digits are not in ascending order.")  # fail
except ValueError:
    print("Error: Please use a 3-digit whole number, no letters")  # not an int
