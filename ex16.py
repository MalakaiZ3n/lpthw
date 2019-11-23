from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

# print("Truncating the file. Goodbye!")
# This step is not actually required if opened in write mode
# target.truncate()

print("Now I'm going to ask you three lines.")

# Input for each line to write
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# Command to write each line of input with a break for each new line
lines = (line1, line2, line3)
target.write('\n'.join(lines))
target.write('\n')


# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()
# Closes the file
