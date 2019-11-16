name = 'Blake Nickens'
age = 42  # not a lie
height = (12 * 5) + 6  # inches
weight = 190  # lbs
eyes = 'blue'
teeth = 'white'
hair = 'shaved'

print(f"Let's talk about {name}.")
print(f"{name} is {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He has {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(
    f"If we add his age of {age}, height of {height}, and weight of {weight} it would be total of {total}.")

# Convert pounds to kilograms
pounds_to_kg = weight * .454

print(
    f"{name}' weight of {weight} pounds would be equal to {pounds_to_kg} kilograms.")
