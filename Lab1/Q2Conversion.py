# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Function to convert temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Taking temperature input in Celsius from the user
celsius = float(input("Enter temperature in Celsius: "))

# Converting Celsius to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Printing the converted temperature in Fahrenheit
print("Temperature in Fahrenheit is:", fahrenheit, "°F")

# Taking temperature input in Fahrenheit from the user
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Converting Fahrenheit to Celsius
celsius = fahrenheit_to_celsius(fahrenheit)

# Printing the converted temperature in Celsius
print("Temperature in Celsius is:", celsius, "°C")