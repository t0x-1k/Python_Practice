from sys import exit
import random

def gold_room():
    print("This room is full of gold, How much do you take?")

    while True:
        try:
            choice = input("> ")
            how_much = int(choice)
    
            if how_much < 50:
                print("Nice, you're not greedy, you win! ")
                exit(0)
            else:
                dead("You greedy bastard")
        except ValueError:
            print("Please enter a valid integer")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey")
    print("The fat bear is in front of another door")
    print("How are you  going to move the bear? ")
    print("You can \033[1;32mtake honey\033[0m or you can \033[1;31mtaunt bear\033[0m")

    bear_moved = random.choice([False, True])

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off ")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. ")
            print("You can go through now ")
            print("If bear moved you can \033[1;32mopen door\033[0m")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off ")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I have no idea what that means")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you \033[1;32mflee\033[0m for your life or eat your \033[1;31mhead\033[0m? ")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty...")
    else:
        cthulhu_room()

def dead(why):
    print(why,"Good job")
    exit(0)

def start():
    print("You are in a dark room. ")
    print("There is a door to your left and right")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve. ")

start()