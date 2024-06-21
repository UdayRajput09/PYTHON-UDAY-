# # Write a Python function to get the largest number, smallest num and sum 
# # of all from a list.

# Creating function
def fun():
    l = [ 4 , 2  , 1  , 7  , 5 ]

    # sorting the list 
    l.sort()
    print(l)

    # printing the smallest and biggest numbers
    print(f"Smallest : {l[0]}")
    print(f"Biggest : {l[-1]}")

    print(f"sum is : {sum(l)}")

# calling function
fun()
