# a Python program to square and cube every number in a given list of integers using Lambda.

numbers = [1, 2, 3, 4, 5]

# Using Lambda to square each number in the list
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Using Lambda to cube each number in the list
cubed_numbers = list(map(lambda x: x**3, numbers))
print(cubed_numbers)  # Output: [1, 8, 27, 64, 125]
