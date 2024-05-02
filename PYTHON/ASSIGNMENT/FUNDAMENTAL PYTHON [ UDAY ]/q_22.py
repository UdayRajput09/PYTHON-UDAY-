
# • Write a Python program to get a string made of the first 2 and the last 
# 2 chars from a given a string. If the string length is less than 2, return 
# instead of the empty string.

# Input string
s = input("Enter a string: ")

# Check if the length of the string is at least 2
if len(s) >= 2:
    # Extract the first 2 and last 2 characters and concatenate them
    result = s[:2] + s[-2:]
else:
    # If the length is less than 2, return an empty string
    result = ""

# Print the result
print("Result:", result)
