#Write a Python program to read a random line from a file.


import random

# Open the file in read mode
file = open('COLLECTION-FUNCTION-MODULES [ UDAY ]\\uday.txt', 'r')
    # Read all lines into a list
lines = file.readlines()
    # Choose a random line from the list
random_line = random.choice(lines)
    # Print the random line
print("Random line from the file:")
print(random_line.strip()) 