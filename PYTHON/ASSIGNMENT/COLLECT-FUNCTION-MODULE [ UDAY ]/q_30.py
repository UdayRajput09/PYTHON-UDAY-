#Write a Python program to check multiple keys exists in a dictionary


# Define the dictionary
dict = {1: 'xyz', 2: 'abc', 3: 'pqr', 4: 'yyy', 5: 'ooo'}

# Keys to check
check = [1, 4, 6]

# Check if each key exists in the dictionary
for i in check:
    if i in dict:
        print(f"The key '{i}' exists in the dictionary.")
    else:
        print(f"The key '{i}' does not exist in the dictionary.")
