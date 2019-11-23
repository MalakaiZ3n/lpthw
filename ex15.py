from sys import argv

script, filename = argv

# open the file defined in the argv
txt = open(filename)

print(f"Here's your file {filename}:")
# reads the text in the file and prints what was in the file
print(txt.read())

# close the text file when done
txt.close()

# print("Type the filename again:")
# file_again = input("> ")

# txt_again = open(file_again)

# print(txt_again.read())
