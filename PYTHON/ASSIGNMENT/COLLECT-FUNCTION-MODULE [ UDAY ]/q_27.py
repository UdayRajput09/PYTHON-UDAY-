# #  Write a Python script to concatenate following dictionaries to create a
# # new one

# Creating two different dictionary
dic1 = {
    1:10,
    2:30,
    3:30
}

dic2 = {
    4:40,
    5:50
}

# Concatenate the two dictionary

concat = {**dic1,**dic2}

#Printing the dictionary
print(f"concatenate the two dictionary : {concat}")

