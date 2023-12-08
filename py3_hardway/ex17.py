from sys import argv
from os.path import exists
from shutil import copyfile

# The script takes three command-line arguments: the script itself, the source file, and the destination file.
script, from_file, to_file = argv

# Open the source file and read its content.
with open(from_file) as in_file:
    in_data = in_file.read()

# Print the size of the source file.
print(f"The input file is {len(in_data)} bytes long")

# Check if the destination file exists.
print(f"Does the output file exist? {exists(to_file)}")

# Copy the source file to the destination file.
copyfile(from_file, to_file)

# Print a message indicating that the operation is complete.
print("Alright, all done")
#
# This code takes three command-line arguments: the script itself, the source file, and the destination file. 
# It then opens the source file, reads its content, and prints the size of the source file. 
# The script checks if the destination file exists and then copies the source file to the destination file. 
# Finally, the script prints a message indicating that the operation is complete.