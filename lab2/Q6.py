#  Try the exercise below:
# 1. Make a program that lists the countries in the set below using a while loop.
# clist = ["Canada","USA","Mexico"]


# 2. What’s the difference between a while loop and a for loop?
# 3. Can you sum numbers in a while loop?
# 4. Can a for loop be used inside a while loop?

clist = ["Canada", "USA", "Mexico"]
i = 0
while i < len(clist):
    print(clist[i])
    i += 1


# The main difference between a while loop and a for loop is the way they iterate over a sequence of values. A for loop is used to iterate over a sequence of values, such as a list or a range of numbers, and the loop variable takes on the values in the sequence automatically. A while loop, on the other hand, is used to execute a block of code repeatedly while a certain condition is true, and the loop variable and condition must be set up manually
# Yes, you can sum numbers in a while loop by initializing a variable to zero before the loop and adding to it inside the loop

# Yes, a for loop can be used inside a while loop.
