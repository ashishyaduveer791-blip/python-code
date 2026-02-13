# Write a program to check whether all the values in a dictionary are same or not using 
# lambda function

# Dictionary
d = {'a': 10, 'b': 10, 'c': 10}

# Lambda function to check all values same
check = lambda x: len(set(x.values())) == 1

# Output
print(check(d))
