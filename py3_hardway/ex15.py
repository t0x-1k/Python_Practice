from sys import argv

# get the script name and filename from the command line arguments
script, filename = argv

# open the file and read its content
txt = open(filename)
print(f"Here's your file {filename}")
print(txt.read())

# close the file
txt.close()

# ask the user to input a filename
filename = input("Please add your filename: ")

# open the file in append mode and write user input to it
with open(filename, 'a') as file:
    user_input = input("Add text here: ")
    file.write(user_input + "\n")

# ask the user to input the filename again
print("Type the filename again: ")
file_again = input("> ")

# open the file again and read its content
txt_again = open(file_again)
print(f"Here is your file again {file_again}")
print(txt_again.read())

# close the second file when done
txt_again.close()
#
#This code allows the user to input a filename, read its content, append new text to it, and then read the updated content. The comments provide a clear and concise explanation of each step in the code..</s>