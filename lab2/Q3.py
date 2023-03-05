# The program must prompt the user for a username and password. The program should
# compare the password given by the user to a known password. If the password matches, the
# program should display “Welcome!” If it doesn’t match, the program should display “I don’t
# know you.
# Note: the password should not be case sensitive and it’s value is abc$123 or ABC$123

# Prompt user for username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Define known password
known_password = "ABC$123"

# Check if entered password matches known password (case insensitive)
if password.upper() == known_password or password.lower() == known_password:
    print("Welcome!")
else:
    print("I don't know you.")
