# Save this code in a file, let's say main.py

a = 1
b = 2

# Import the add function from add_0.py
from add_0 import add

# Print the result using string format
print("{} + {} = {}".format(a, b, add(a, b)))
