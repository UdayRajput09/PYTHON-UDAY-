# Write a Python program to count the frequency of words in a file.


import re
from collections import Counter

# Path to the input file
file_path = 'C:/Users/HP/OneDrive/Documents/Full Stack/PYTHON/ASSIGNMENT/ADVANCE PYTHON [ UDAY ]/demo.txt.txt'

# Read the file and count word frequencies
with open(file_path, 'r') as file:
    text = file.read().lower()  # Read the file content and convert to lowercase

# Use regular expressions to find all words (alphanumeric sequences)
words = re.findall(r'\b\w+\b', text)

# Count the frequency of each word
word_count = Counter(words)

# Print the word frequencies
for word, count in word_count.items():
    print(f'{word}: {count}')
