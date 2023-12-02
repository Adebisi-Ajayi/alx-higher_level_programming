#!/usr/bin/python3
from sys import argv
arguments = [int(arg) for arg in argv[1:]]
result = sum(arguments)
print(result)
