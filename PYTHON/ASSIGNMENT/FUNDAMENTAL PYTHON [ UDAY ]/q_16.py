# Write a Python program to count the occurrences of each word in a
# given sentence

# Take input from the user
# Take input from the user
s = input("Enter a sentence: ")

# Split the sentence into words
w = s.split()

# Create an empty dictionary to store word counts
d = {}

# Iterate through each word in the sentence
for word in w:
    # If the word is already in the dictionary, increment its count
    if word in d:
        d[word] += 1
    # If the word is not in the dictionary, add it with a count of 1
    else:
        d[word] = 1

# Print the word counts
for word, count in d.items():
    print(f"{word}: {count}")

