import datetime

# Create a datetime object
now = datetime.datetime.now()

# Lambda functions to extract year, month, date, and time
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
time = lambda x: x.time()

# Testing the Lambda functions with the datetime object
print(year(now))   # Output: 2023
print(month(now))  # Output: 3
print(day(now))    # Output: 5
print(time(now))   # Output: 18:10:30.868064