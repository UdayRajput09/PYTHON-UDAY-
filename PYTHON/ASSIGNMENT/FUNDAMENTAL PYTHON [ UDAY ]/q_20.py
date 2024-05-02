# Write a Python function that takes a list of words and returns the length 
# of the longest one.

def longest_length(words):
    # Initialize the maximum length variable
    max_len = 0
    
    # Iterate through each word in the list
    for w in words:
        # Check if the length of the current word is greater than the maximum length found so far
        if len(w) > max_len:
            # If yes, update the maximum length
            max_len = len(w)
    
    # Return the maximum length
    return max_len

# Test the function
word_list = ["apple", "banana", "orange", "strawberry"]
print("Length of the longest word:", longest_length(word_list))

