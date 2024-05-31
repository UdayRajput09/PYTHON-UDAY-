# Write a Python program to get unique values from a list

# creating list 1
l = [ 1 , 2 , 3 , 4 , 5 , 1 , 2 , 3 ]

# crating empty list 2
l1 = []

# for loop for getting unique value from list 1
for i in l:
    if i not in l1:
        l1.append(i)

# printing unique value in list 2
print(f"Unique number in list are : {l1}")