# name variable formatter of 4 strings
formatter = "{} {} {} {}"

# return a different format version of the formatter string variable

# each field is a digit
print(formatter.format(1, 2, 3, 4))

# each field is string of text
print(formatter.format("one", "two", "three", "four"))

# each field is a boolean
print(formatter.format(True, False, False, True))

# each field is the orginal variable string
print(formatter.format(formatter, formatter, formatter, formatter))


print(formatter.format(
    "You can dance if you want to",
    "You can leave your friends behind",
    "It's safe to dance",
    "Safety Dance!!!"
))
