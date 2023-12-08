while True:
    try:
        age = int(input("How old are you? "))
        height = int(input("How tall are you? "))
        weight = int(input("How much do you weigh? "))
    except ValueError:
        print("Must be an integer!")
        continue
    else:
        break

#update to allow the user both ints and strings
print(f"So you are {age} years old, {height} inches tall, and weigh {weight} pounds")
