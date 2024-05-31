# Write a Python program to generate and print a list of first and last 5 
# elements where the values are square of numbers between 1 and 30.


# Creating empty list
l = []

# for loop for check square 
for i  in range (1,31):
    j = i ** 2
    l.append(j)


# printing first 5 element 
print("First 5 element of List : ",l[:5])


# printing last 5 element 
print("Last 5 element of List : ",l[-5:])