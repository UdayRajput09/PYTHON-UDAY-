# Write a Python program to unzip a list of tuples into individual lists.


# Creating list with tuples 
l = [ (1 , 2 , 3) , ( 4 , 5 , 6 ) , ( 'a' , 'b' , 'c' ) , ( 'x' , 'y' , 'z' ) ]

# unzip tuples
unzip = list(zip(*l))

# unzip tuples into different lists
unzip = [ list(i) for i in unzip]

# printing list
print(unzip)