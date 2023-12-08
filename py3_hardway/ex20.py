from sys import argv

# obtain the script name and input file name from the command line arguments
script, input_file = argv

# define a function to print all the contents of a file
def print_all(f):
    print(f.read())

# define a function to rewind a file to the beginning
def rewind(f):
    f.seek(0)

# define a function to print a specific line from a file
def print_a_line(line_count, f):
    print(line_count, f.readline())

# open the input file for reading
current_file = open(input_file)

# print the whole file
print("First let's print the whole file: \n")
print_all(current_file)

# rewind the file to the beginning
print("Now let's rewind, kind of like a tape")
rewind(current_file)

# print three lines from the file
print("Let's print three lines \n")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

# In this code, we first obtain the script name and input file name from the command line arguments. Then, we define three functions: `print_all`, `rewind`, and `print_a_line`. 
# The `print_all` function reads and prints the entire contents of a file. 
# The `rewind` function moves the file pointer to the beginning of the file. The `print_a_line` function prints a specific line from the file.
# Next, we open the input file for reading and use the `print_all` function to print the entire file