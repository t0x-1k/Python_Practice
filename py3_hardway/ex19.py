def cheese_and_crackers(cheese_count, boxes_of_crackers):
    """
    This function takes two arguments, cheese_count and boxes_of_crackers, 
    and prints a message about the number of cheeses and crackers.
    """
    print(f"You have {cheese_count} cheeses")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("Man that's enough for a party!")
    print("Get a blanket \n")

# Call the function cheese_and_crackers with two numbers directly
print("We can just give the functions numbers directly: ")
cheese_and_crackers(20, 50)

# Call the function cheese_and_crackers with two variables
print("OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

# Call the function with the variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Call the function with math inside the function call
print("We can even do math inside too: ")
cheese_and_crackers(10 + 20, 5 + 6)

# Call the function with a combination of variables and math
print("And we can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#
# In this code, the function `cheese_and_crackers` takes two arguments, `cheese_count` and `boxes_of_crackers`, and prints a message about the number of cheeses and crackers.
#
# The function is then called with different arguments, such as two numbers directly, two variables, math inside the function call, and a combination of variables and math.