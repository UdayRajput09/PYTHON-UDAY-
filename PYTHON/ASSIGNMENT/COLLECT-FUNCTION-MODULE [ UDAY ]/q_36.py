# Write a Python program to find the highest 3 values in a dictionary


# Sample dictionary
data = {'a': 7, 'b': 2, 'c': 5, 'd': 3, 'e': 4}

# Get the values from the dictionary
vals = list(data.values())

# Sort the values in descending order
vals.sort(reverse=True)

# Get the highest 3 values
top_vals = vals[:3]

# Find the keys corresponding to the highest values
top_keys = [k for k, v in data.items() if v in top_vals]

# Print the highest 3 values and their keys
print("Highest 3 values in the dictionary:")
for k, v in zip(top_keys, top_vals):
    print(k, "=", v)

