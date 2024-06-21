# Write a Python program to print all unique values in a dictionary.


# Define the dictionary
d = {1: 'abc', 2: 'xyz', 3: 'pqr', 3: 'yyy', 4: 'ooo'}

# Initialize a set to store unique values
unique = set()

# Iterate over the values of the dictionary and add them to the set
for i in d.values():
    unique.add(i)

# Print the unique values
print("Unique Values:", unique)
