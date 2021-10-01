"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 14 Sep 2021
Homework Problem # 2_1
Work through order of operations and use constructors for casting types
"""

num = int(input("Give a number 1 to 9: "))  # prompt for num 1-9
num_with_math = ((((num * 2) + 10) / 2) - num)  # do math
print(int(num_with_math), "is the number after all the math")  # print as int
three_digit = str(int(num_with_math)) * 3  # make it 3 repeating digits
sum_three_digit = num_with_math + num_with_math + num_with_math  # + digits
div = int(three_digit) / int(sum_three_digit)  # 3 digit num / by sum of digits
print(int(div),  "is the number after more math")  # print as int
