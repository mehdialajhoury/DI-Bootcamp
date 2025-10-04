# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.

# Lists:

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# Expected Output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary = dict(zip(keys, values))

print(dictionary)