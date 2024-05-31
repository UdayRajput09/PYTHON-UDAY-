# # Write a Python program to find the maximum and minimum numbers
# from the specified decimal numbers.


def get_max_min(nums):
    # Find the maximum number in the list
    max_num = max(nums)
    # Find the minimum number in the list
    min_num = min(nums)
    # Return the maximum and minimum numbers
    return max_num, min_num

# Test the function with a list of numbers
num_list = [5.345, 1.234, 7.894, 2.564, 9.999]
# Call the function to find the maximum and minimum numbers
max_value, min_value = get_max_min(num_list)

# Print the maximum and minimum numbers
print("Maximum number:", max_value)
print("Minimum number:", min_value)

