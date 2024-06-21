# Write a Python function that takes two lists and returns true if they have 
# at least one common member

# Creating function
def fun():

    #creating list
    l1 = [1, 2, 3, 4, 5]
    l2 = [6, 7, 8, 9, 1]

    # for loop for checking condition
    for i in l1:
        if i in l2:
            return True
    return False


# calling function
print(fun())

