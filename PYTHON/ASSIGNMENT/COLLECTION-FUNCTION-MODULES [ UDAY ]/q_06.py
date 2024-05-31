# Write a Python program to count the number of strings where the string 
# length is 2 or more and the first and last character are same from a given 
# list of strings.



# Creating the list
l = ["abc" , "xyz" , "pqr" , "aaa" , "zzz" , "rrr"]

# count = 0
count = 0


# for loop for increment of  count
for i in l :
    if len(i)>2 and i[0] == i[-1]:
        count += 1

# printing count 
print("Number of string where first and last character are same is : ",count)