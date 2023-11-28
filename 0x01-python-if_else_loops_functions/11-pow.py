#!/usr/bin/python3
def pow(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

power_result = pow(2, 3)
print("Result:", power_result)
