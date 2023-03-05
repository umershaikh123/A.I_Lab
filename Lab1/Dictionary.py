# Define the input dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create a new dictionary and use the update() method to add the input dictionaries to it
new_dict = {}
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

# Print the final dictionary
print(new_dict)