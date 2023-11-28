# Print the ASCII alphabet in lowercase without a new line

# Loop through the ASCII values for lowercase letters (97 to 122)
for i in range(97, 123):
    # Use the chr() function to convert the ASCII value to a character
    # Use the end parameter of the print function to avoid a new line
    print(chr(i), end='')

# Print a new line after printing all the characters
print()

