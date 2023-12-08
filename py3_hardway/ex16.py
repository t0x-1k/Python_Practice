from sys import argv

# This script takes a filename as a command line argument and opens it in write mode.
script, filename = argv

print("Opening the file...")

target = open(filename, 'w')

print("Now I'm going to ask you for three lines. ")
# It then prompts the user to enter three lines of text.
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to file.")
# These lines are written to the file and the file is closed.
target.write(f"{line1}\n{line2}\n{line3}")

print("And finally, we close it.")

target.close()
#
# This code takes a filename as a command line argument and opens it in write mode. 
# It then prompts the user to enter three lines of text. These lines are written to the file and the file is closed. 
