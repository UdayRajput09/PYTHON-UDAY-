# • Write a Python program to remove an empty tuple(s) from a list of tuples


# creating list of tuples
l = [ (1 , 2 , 3 ) , ( ) , (1 , 2 , 3 ) , ( )]

# creating empty list
l1 = [ ]

# loop for removing empty tuple from the list
for i in l:
    if i :
        l1.append(i)


# printing new list without empty tuples
print(l1)