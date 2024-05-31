# Write a Python program to remove duplicates from a list.


# Creating list
l = [ 1 , 2 , 4 , 6 , 8, 1 , 2 , 4 ]

# Crating empty list for after remove duplicate number
l1 = []

# For loop for append the unique number in l1 
for i in l:
    if i not in l1:
        l1.append(i)
    
# printing l1 
print(l1)