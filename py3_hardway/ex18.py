def print_two(*args):
    """
    This function takes any number of arguments and prints them.
    It assumes that at least two arguments are provided.
    """
    arg1, arg2 = args
    print(f"arg1: {arg1} arg2: {arg2}")

def print_two_again(arg1, arg2):
    """
    This function takes exactly two arguments and prints them.
    It is similar to print_two, but it does not use variable arguments.
    """
    print(f"arg1: {arg1} arg2: {arg2}")

def print_one(arg1):
    """
    This function takes one argument and prints it.
    """
    print(f"arg1: {arg1}")

def print_none():
    """
    This function takes no arguments and prints a message.
    """
    print("I got nothing.")

print_two("zed", "shaw")
print_two_again("zed", "shaw")
print_one("First")
print_none()
#
# In this code, we have four functions that print different numbers of arguments. 
# Each function has a docstring that provides a clear and concise explanation of its purpose and behavior. 
# This will help you stay focused and informed about the code you are working with.