# Write a Python program to replace last value of tuples in a list.

# Example list of tuples
list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
new_value = 10  # The value to replace the last element with

# Iterate over the list and replace the last value of each tuple
for i in range(len(list_of_tuples)):
    # Convert tuple to list to allow modification
    temp_list = list(list_of_tuples[i])
    # Replace the last element
    temp_list[-1] = new_value
    # Convert list back to tuple and update the list
    list_of_tuples[i] = tuple(temp_list)

# Print the modified list of tuples
print(list_of_tuples)
