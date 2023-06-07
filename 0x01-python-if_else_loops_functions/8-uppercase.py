#!/usr/bin/python3
def uppercase(str):
    for c in str:
        ascii_val = ord(c)
        if 97 <= ascii_val <= 122:
            upper_ascii = ascii_val - 32
            print(chr(upper_ascii), end="")
        else:
            print(c, end="")
            print()
