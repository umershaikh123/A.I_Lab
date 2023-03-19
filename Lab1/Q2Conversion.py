# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Function to convert temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

 
celsius = float(input("Enter temperature in Celsius: "))

 
fahrenheit = celsius_to_fahrenheit(celsius)
 
print("Temperature in Fahrenheit is:", fahrenheit, "°F")

 
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

 
celsius = fahrenheit_to_celsius(fahrenheit)

 
print("Temperature in Celsius is:", celsius, "°C")