def add(a, b):
    """
    This function takes two numbers as input and returns their sum.
    It also prints a message indicating the numbers being added.
    """
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    """
    This function takes two numbers as input and returns the result of subtracting the second number from the first.
    It also prints a message indicating the numbers being subtracted.
    """
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    """
    This function takes two numbers as input and returns their product.
    It also prints a message indicating the numbers being multiplied.
    """
    print(f"Multiply {a} * {b}")
    return a * b

def divide(a, b):
    """
    This function takes two numbers as input and returns the result of dividing the first number by the second.
    It also prints a message indicating the numbers being divided.
    """
    print(f"Dividing {a} / {b}")
    return a / b

print("Let's do some math with just functions\n")

# Calculate age, height, weight, and IQ using the functions defined above
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print()

print(f"Age: {age} Height: {height} Weight: {weight} IQ: {iq} \n")

print("Here is a puzzle: \n")

#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

#more readability from line 48
result_division = divide(iq, 2)
result_multiplication = multiply(weight, result_division)
result_subtraction = subtract(height, result_multiplication)
what = add(age, result_subtraction)

print()

print(f"That becomes: {what} Can you do it by hand")