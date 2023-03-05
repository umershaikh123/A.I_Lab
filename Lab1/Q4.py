 # Define a list of strings
string_list = ['abc', 'xyz', 'aba', '1221']

# Define a counter variable to keep track of the number of strings
count = 0

# Loop through each string in the list
for string in string_list:
    # Check if the length of the string is greater than or equal to 2
    if len(string) >= 2:
        # Check if the first and last characters of the string are the same
        if string[0] == string[-1]:
            # If the conditions are met, increment the counter
            count += 1

# Print the final count
print("Number of strings with length 2 or more and first and last characters the same:", count)