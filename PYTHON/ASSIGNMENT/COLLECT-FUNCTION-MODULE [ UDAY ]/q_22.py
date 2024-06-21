# # Write a Python program to find the repeated items of a tuple.

# # Creating tuple
t = ( 1 , 2 , 3 , 4 , 5 , 1 , 2 )


# Creating sets 
t1 = set()

t2 = set()

# looping for adding 
for i in t:
    if i in t1 :
        t1.add(i)
    else:
        t2.add(i)

# printing 
print(t)
print(t1)
print(t2)  


