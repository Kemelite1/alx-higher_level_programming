#!/usr/bin/python3
for first_number in range(10):
    for second_number in range(first_number + 1, 10):
        print("{:d}{:d}, ".format(first_number, second_number), end="")
print()
