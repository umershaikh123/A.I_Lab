# a Python program to find if a given string starts with a given character using Lambda.

starts_with_char = lambda string, char: string[0] == char

# Testing the Lambda function with sample data
string1 = "Hello, world!"
char1 = "H"
print(starts_with_char(string1, char1))  # Output: True

string2 = "Python is awesome!"
char2 = "p"
print(starts_with_char(string2, char2))  # Output: False