# Write a Python program to find the first appearance of the substring 
# 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
# whole 'not'...'poor' substring with 'good'. Return the resulting string.

# Input string
s = input("Enter a string: ")

# Find the index of 'not' and 'poor' in the string
n = s.find('not')
p = s.find('poor')

# Check if both 'not' and 'poor' are present and 'not' comes before 'poor'
if n != -1 and p != -1 and n < p:
    # Replace the substring from 'not' to 'poor' with 'good'
    m = s[:n] + 'good' + s[p + 4:]
else:
    # If 'not' and 'poor' are not found or 'not' comes after 'poor', use the original string
    m = s

# Print the resulting string
print("Result:", m)
