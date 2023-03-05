# Define the input list
input_list = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'PHP', 'HTML', 'CSS']

# Use list comprehension to generate the lowercased version of each string that has length greater than five
output_list = [string.lower() for string in input_list if len(string) > 5]

# Print the final list
print(output_list)