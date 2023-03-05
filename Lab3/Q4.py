# Open the file in write mode
with open("city_data.txt", "w") as f:

    # Get the number of cities from the user
    num_cities = int(input("Enter the number of cities: "))

    # Loop over each city
    for i in range(num_cities):

        # Get the city data from the user
        city_name = input("Enter the name of the city: ")
        population = int(input("Enter the population of the city: "))
        mayor = input("Enter the name of the mayor: ")

        # Write the city data to the file
        f.write(city_name + "," + str(population) + "," + mayor + "\n")

print("City data written to file successfully.")
