# Write a program to create two lists and generate a dictionary with keys from list1 and 
# values from list2. 


# Create two lists
list1 = ['a', 'b', 'c']
list2 = [10, 20, 30]

# Create dictionary using zip()
result = dict(zip(list1, list2))

# Print dictionary
print(result)
