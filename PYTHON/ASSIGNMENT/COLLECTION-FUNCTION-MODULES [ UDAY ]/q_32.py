# Write a Python script to sort (ascending and descending) a dictionary by 
# value.

# Example dictionary
example_dict = {
    'apple': 5,
    'banana': 2,
    'cherry': 7,
    'date': 3,
    'elderberry': 1
}

# Sort and print dictionary by value in ascending order
print("Ascending order:", dict(sorted(example_dict.items(), key=lambda item: item[1])))

# Sort and print dictionary by value in descending order
print("Descending order:", dict(sorted(example_dict.items(), key=lambda item: item[1], reverse=True)))
