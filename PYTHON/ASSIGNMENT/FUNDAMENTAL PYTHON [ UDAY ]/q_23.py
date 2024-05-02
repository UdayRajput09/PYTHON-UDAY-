# • Write a Python function to insert a string in the middle of a string.
def insert_middle(s, ins):
    # Calculate the middle index of the main string
    m = len(s) // 2
    
    # Insert the string in the middle of the main string
    r = s[:m] + ins + s[m:]
    
    # Return the result
    return r

# Test the function
s = "Hello, World!"
ins = "Python"
result = insert_middle(s, ins)
print("Result:", result)
