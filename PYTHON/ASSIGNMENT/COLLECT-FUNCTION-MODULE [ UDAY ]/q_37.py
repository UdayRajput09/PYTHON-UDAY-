# Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
# 300}, o {'item': 'item1', 'amount': 750}]
# Expected Output:
# Counter ({'item1': 1150, 'item2': 300})


# Sample data
data_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# Combine values
result = {}

for entry in data_list:
    item = entry['item']
    amount = entry['amount']
    if item in result:
        result[item] += amount
    else:
        result[item] = amount

# Print the combined values
print("Combined values:")
print(result)

