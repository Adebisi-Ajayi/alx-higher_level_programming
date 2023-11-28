#!/usr/bin/python3
for tens_digit in range(10):
    for ones_digit in range(tens_digit + 1, 10):
        print("{:02}, ".format(tens_digit * 10 + ones_digit), end="")
print ()
