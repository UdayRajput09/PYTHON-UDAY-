# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string: 'w3resource'
# Expected output:
# {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}



# Sample string
string = 'w3resource'

# Initialize an empty dictionary to store letter counts
l = {}

# Iterate through each character in the string
for i in string:
    # Increment the count of the character in the dictionary
    l[i] = l.get(i, 0) + 1

# Print the dictionary
print("Dictionary with letter counts:")
print(l)

