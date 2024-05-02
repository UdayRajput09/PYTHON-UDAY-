# • Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string

# Get input strings from the user
# Input strings
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

# Swap the first two characters of each string and concatenate them
result = s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]

# Print the result
print("Result:", result)
