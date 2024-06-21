# Write a Python program to check whether an element exists within a 
# tuple.

# Creating tuple 
t = ( 1 , 2 , 3 , 4 , 5 )

# creating check named variable and assigning value 5 for checking
check = 5

# if-else for checking that check variable value in tuple 
if check in t :
    print(f"{check} is in tuple")
else:
    print(f"{check} is not in tuple")