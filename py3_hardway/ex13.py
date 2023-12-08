from sys import argv
#updated to allow user input in both int and strings
script, first, second, third = argv

try:
    first = int(first)
except:
    pass
try:
    second = int(second)
except:
    pass
try:
    third = int(third)
except:
    pass



print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)
