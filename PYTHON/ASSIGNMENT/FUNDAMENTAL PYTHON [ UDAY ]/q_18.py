# Write a Python program to add 'ing' at the end of a given string (length 
# should be at least 3). If the given string already ends with 'ing' then add 
# 'ly' instead if the string length of the given string is less than 3, leave it 
# unchanged.

# Input string
s = input("Enter a string: ")

# Check if the length of the string is at least 3 and it ends with 'ing'
if len(s) >= 3 and s.endswith('ing'):
    # If yes, add 'ly' at the end
    modified = s + 'ly'
elif len(s) >= 3:
    # If the length is at least 3 but doesn't end with 'ing', add 'ing' at the end
    modified = s + 'ing'
else:
    # If the length is less than 3, leave it unchanged
    modified = s

# Print the modified string
print("Modified string:", modified)
