# Creating a list of numbers
numbers = [3, 7, 2, 8, 1, 5, 9, 4, 6]

# Printing the original list
print("Original list of numbers:", numbers)

# Using the sort() function to sort the list in ascending order
numbers.sort()
print("Sorted list of numbers:", numbers)

# Using the reverse() function to reverse the order of the list
numbers.reverse()
print("Reversed list of numbers:", numbers)

# Using the append() function to add a new element to the end of the list
numbers.append(10)
print("List of numbers after appending 10:", numbers)

# Using the insert() function to insert a new element at a specific index in the list
numbers.insert(0, 0)
print("List of numbers after inserting 0 at index 0:", numbers)

# Using the pop() function to remove the last element from the list and return it
last_number = numbers.pop()
print("List of numbers after popping the last element:", numbers)
print("Popped element from the list:", last_number)

# Using the remove() function to remove a specific element from the list
numbers.remove(8)
print("List of numbers after removing 8:", numbers)