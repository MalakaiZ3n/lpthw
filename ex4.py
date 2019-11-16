cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90

# The number of cars available less how many drivers that use them
cars_not_driven = cars - drivers

# The cars driven is equal to the number of drivers
cars_driven = drivers

# Available cars driven multiplied by space in each car
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "passengers to carpool today.")
print("We need to put about", average_passengers_per_car, "passengers in each car.")
