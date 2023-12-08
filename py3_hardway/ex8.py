
# Define a formatter string with placeholders for each value
formatter = "{} {} {} {}"

# Use the formatter string to print a combination of integers
print(formatter.format(1,2,3,4))

# Use the formatter string to print a combination of strings
print(formatter.format("one", "two", "three", "four"))

# Use the formatter string to print a combination of booleans
print(formatter.format(True, False, False, True))

# Use the formatter string to print a combination of the formatter string itself
print(formatter.format(formatter, formatter, formatter, formatter))

# Use the formatter string to print a combination of strings and placeholders
print(formatter.format(
    "Try your",
    "own code here",
    "and see what happens!",
    "just needed one more" 
))
#
#In this code, we define a formatter string with placeholders for each value. 
# We then use the formatter string to print a combination of different data types, including integers, strings, booleans, and even the formatter string itself. 
