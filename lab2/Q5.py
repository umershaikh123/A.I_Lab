# Try the scenrio below:
# Make a program that lists the countries in the set
# clist =
# ['Canada','USA','Mexico','Australia']
# 1. Create a loop that counts from 0 to 100
# 2. Make a multiplication table using a loop
# 3. Output the numbers 1 to 10 backwards using a loop
# 4. Create a loop that counts all even numbers to 10
# 5. Create a loop that sums the numbers from 100 to 200

clist = ['Canada', 'USA', 'Mexico', 'Australia']

for country in clist:
    print(country)


for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end='\t')
    print()

for i in range(10, 0, -1):
    print(i)


count = 0

for i in range(1, 11):
    if i % 2 == 0:
        count += 1

print("There are", count, "even numbers from 1 to 10")


sum = 0

for i in range(100, 201):
    sum += i

print("The sum of numbers from 100 to 200 is", sum)
