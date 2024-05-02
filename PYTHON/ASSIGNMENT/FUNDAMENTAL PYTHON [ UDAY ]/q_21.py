# Write a Python function to reverses a string if its length is a multiple of 
# 4.

def reverse_if_multiple_of_four(s):
    # Check if the length of the input string is a multiple of 4
    if len(s) % 4 == 0:
        # If yes, reverse the string
        return s[::-1]
    else:
        # If not, return the original string
        return s

# Test the function
test_string = "abcdef"
print("Original:", test_string)
print("Reversed if multiple of 4:", reverse_if_multiple_of_four(test_string))

