#!/usr/bin/python3
# Print ASCII alphabet in lowercase without a new line
print(''.join(chr(i) for i in range(ord('a'), ord('z') + 1)), end='')

