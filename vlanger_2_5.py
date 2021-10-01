"""
Vicki Langer
Class: CS 521 - Fall 1
Date: 14 Sep 2021
Homework Problem # 2_5
variation of fizz buzz
"""

# test success numbers: 6, 10, 15, 30, 45
# test fail numbers: 29, 7, 13

count = 0  # starting counter
number = 30  # constant num for for loop iterations

for i in range(1, number):
    print(f"{i}:",  # label the output
          "foo" * (i % 2 == 0),  # if divisible by 2 print foo
          "bar" * (i % 3 == 0),  # if divisible by 3 print bar
          "baz" * (i % 5 == 0),  # if divisible by 5 print baz
          "" * (count % 3 != 0) and
               (count % 3 != 0) and
               (count % 5 != 0),  # if !divisible by 2,3,nor 5 print empty str
          )
    i = i + 1  # add 1 to iteration var

print("-"*10)  # seperator line

# do it all again, but with a while loop

while count < number:
    print(f"{count}:",  # label the output
          "foo" * (count % 2 == 0),  # if divisible by 2 print foo
          "bar" * (count % 3 == 0),  # if divisible by 3 print bar
          "baz" * (count % 5 == 0),  # if divisible by 5 print baz
          "" * (count % 3 != 0) and
               (count % 3 != 0) and
               (count % 5 != 0),  # if !divisible by 2,3,nor 5 print empty str
          )
    count = count + 1  # add 1 to iteration var
