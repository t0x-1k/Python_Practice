def while_function(limit, increment):
    i = 0
    numbers = []
    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        print(numbers)
        i += increment

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    print("The numbers: ")

    for numb in numbers: 
        print(numb)


while_function(12, 2)