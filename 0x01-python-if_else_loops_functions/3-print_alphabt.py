#!/usr/bin/python3
alphabet = ''.join(chr(letter) for letter in range(ord('a'), ord('z') + 1) if chr(letter) != 'q' and chr(letter) != 'e')
print("{}".format(alphabet), end='')
