# # Write a Python function that checks whether a passed string is
# palindrome or not

# sample input = radar


def pal(s):
    return s == s[::-1]

# Ask the user for input
string = input("Enter a string: ")

# Check if the string is a palindrome and print the result
if pal(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
    