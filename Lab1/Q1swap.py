# Taking input values of a, b, c, and d from the user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
d = int(input("Enter the value of d: "))

# Swapping the values of a, b, c, and d using temporary variable
temp = a
a = d
d = temp
temp = b
b = c
c = temp

# Printing the swapped values of a, b, c, and d
print("After Swapping")
print("a = ", a, ", b = ", b, ", c = ", c, ", d = ", d)