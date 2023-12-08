from sys import exit
import random

#define all dungeons those paths lead to
def Rappan_Athuk():
    print("You made it to Rappan Athuk")
    print()
    print("You stand in front of two doors. ")
    print("Do you chose door number: 1")
    print("Or, do you chose door number: 2")

    door_choice = input("> ")

    if door_choice == "1":
        print("A goblin stand in front of you and the exit.")
        print("What do you do?")
        print("Scream ")
        print("Or, Throw chair")
        goblin_moved = random.choice([False, True])

    while True:       
        room_choice = input("> ").strip().lower() 

        if room_choice == "scream" and not goblin_moved:
            dead("The goblin ate your head...")
        elif room_choice == "scream" and goblin_moved:
            print("The goblin ran away in fear of your tone. ")
            goblin_moved = True
            Barrowmaze()     
        elif room_choice == "throw chair" and not goblin_moved:
            dead("The goblin catches chair and beats you with it...")
        elif room_choice== "throw chair" and goblin_moved:
            print("The goblin is now unconscious, you may move on")
            goblin_moved = False
            Barrowmaze()
        else:
            break

    if door_choice == "2":
        print("You walk in a room with a treasure chest sitting in the middle of the room. ")
        print("Do you open the chest: Yes")
        print("Do you walk out the door with an eerie feeling of something bad: Walk out ")
        mimic_moved = random.choice([False, True])

    while True:   
        room_choice = input("> ").strip().lower()

        if room_choice == "yes" and not mimic_moved:
            dead("You realize it is a mimic and it eats you...")
        elif room_choice == "yes" and mimic_moved:
            print("You open the chest and false wall opens up for you to walk through\n")
            mimic_moved = True
            Barrowmaze()         
        elif room_choice == "walk out" and not mimic_moved:
            dead("The mimic chases you down and you still die...")    
        elif room_choice == "walk out" and mimic_moved:
            print("You found another way around")
            mimic_moved = False
            Barrowmaze()
        else:
            break 

def Tegel_Manor():
    print("You have made it to Tegel Manor")
    print("You have three doors to choose from.")
    print("Do you chose door: 1")
    print("Do you chose door: 2")
    print("Or, do you chose door: 3")
    
    door_choice = input("> ")

    if door_choice == "1":
        print("You enter a room that has a large table in the center. ")
        print("Do you walk over and inspect the: table")
        print("Or, do you: leave")
        collapsed_roof = random.choice([False, True])
    
    while True:
        room_choice = input("> ").strip().lower()

        if room_choice == "table" and not collapsed_roof:
            dead("The roof collapsed on your head...")
        elif room_choice == "table" and collapsed_roof:
            print("You notice the roof is collapsing and you quickly slide under the table to survive")
            collapsed_roof = True
            Barrowmaze()
        elif room_choice == "leave" and not collapsed_roof:
            dead("You thought too hard about your decision and the roof collapsed on your head...")
        elif room_choice == "leave" and collapsed_roof:
            print("You made it out in the nick of time. ")
            collapsed_roof = False
            Barrowmaze()
        else:
            break
        
    if door_choice == "2":
        print("You walk into an ordinary looking room. ")
        print("You notice fireplace in the corner")
        print("Do you approach the: fireplace")
        print("Or, do you inspect the: chest")
        compacting_walls = random.choice([False, True])

    while True:
        room_choice = input("> ").strip().lower()

        if room_choice == "fireplace" and not compacting_walls:
            dead("You grabbed grabbed the wrong candlestick and the compacting walls crushed you...")
        elif room_choice == "fireplace" and compacting_walls:
            print("You light the fire and secret passage opens up behind the fireplace for you to escape")
            compacting_walls = True
            Barrowmaze()
        elif room_choice == "chest" and not compacting_walls:
            dead("Those coins are not for you, the compacting walls crush you to death...")
        elif room_choice == "chest" and compacting_walls:
            print("You decide to take nothing and shut the lid, a passage opens up behind the fireplace")
            compacting_walls = False
            Barrowmaze()
        else:
            break

    if door_choice == "3":
        print("You find yourself in a dark hallway.")
        print("Do you continue down the: hallway")
        print("Or, do you find another way: around")
        poison_darts = random.choice([True, False])

    while True:
        room_choice = input("> ").strip().lower()

        if room_choice == "hallway" and not poison_darts:
            dead("The first stone you step on sinks and poison darts fly from the walls killing you...")
        elif room_choice =="hallway" and poison_darts:
            print("You make it to the end of the hallway and find and exit")
            poison_darts = True
            Barrowmaze()
        elif room_choice == "around" and not poison_darts:
            dead("You run around in circles and accidentally step on the trapped stone releasing the poison darts killing you...")
        elif room_choice == "around" and poison_darts:
            print("You fumble around long enough and find an exit")
            poison_darts = False
            Barrowmaze()
        else:
            break

     
def Stonehell_Dungeon():
    print("You made it to Stonehell Dungeon")
    print("You have three doors to choose from.")
    print("1) Door 1 - A small wooden door with rusty hinges")
    print("2) Door 2 - A large iron door with intricate carvings")
    print("3) Door 3 - A heavy oak door with ancient runes etched into its surface")

    door_choice = input("> ")

    if door_choice == "1":
        print("You open the small squeaky door to reveal a tiny bedroom")
        print("There is a single bed in the center of the room")
        print("Do you feel tired and take a: nap")
        print("Or, inspect the room: further")
        exploding_tiles = random.choice([False, True])

    while True:
        room_choice = input("> ").strip().lower()

        if room_choice == "nap" and not exploding_tiles:
            dead("You step on the first cobblestone and it explodes in your face...")
        elif room_choice == "nap" and exploding_tiles:
            print("You fall asleep for hours and wake up to find you have been transported.")
            exploding_tiles = True
            Barrowmaze()
        elif room_choice == "further" and not exploding_tiles:
            dead("You should really watch where you step...")
        elif room_choice == "further" and exploding_tiles:
            print("As you explore the room, you notice a window for you to escape from.")
            exploding_tiles = False
            Barrowmaze()
        else:
            break

    if door_choice == "2":
        print("You open the large iron door to reveal a grand throne room")
        print("A giant stone statue of a dragon stands atop a dais in front of the throne")
        print("Do you approach the statue: approach")
        print("Or do you sit on the throne: throne")
        beholder = random.choice([False, True])

    while True:
        room_choice = input("> ").strip().lower()

        if room_choice == "approach" and not beholder:
            dead("A beholder emerges from the darkness and kills you with a death ray...")
        elif room_choice == "approach" and beholder:
            print("The beholder looks at you with cold eyes and disappears and the stone dragon reveals a door.")
            beholder = True
            Barrowmaze()
        elif room_choice == "throne" and not beholder:
            dead("You have a seat at the throne and the dragon awakens a beholder and turns you to stone...")
        elif room_choice == "throne" and beholder:
            print("You sit at the throne and feel a button on the arm of the throne that reveals a passage behind the stone dragon")
            beholder = False
            Barrowmaze()
        else:
            break

    if door_choice == "3":
        print("The hallway opens into a large chamber filled with treasure chests")
        print("Do you search through the piles of gold and jewels: treasure")
        print("Or do you continue down the hallway: hallway")
        Illithid = random.choice([False, True])

    while True:
        room_choice = input("> ").strip().lower()

        if room_choice == "treasure" and not Illithid:
            dead("An illithid attacks you and absorbs your soul...")
        elif room_choice == "treasure" and Illithid:
            print("You find a magical amulet that grants you immunity from the Illithid and you escape")
            Illithid = False
            Barrowmaze()
        elif room_choice == "hallway" and not Illithid:
            dead("You hear footsteps behind you and turn around to see an illithid sucking the health from your body...")
            Illithid = True
        elif room_choice == "hallway" and Illithid:
            print("You escape the Illithid by finding a secret passage way out")
            Illithid = False
            Barrowmaze()
        else:
            break

def Temple_of_Black_Earth():
    print("You made it to Temple of Black Earth")
    print("There are two doors in front of you.")
    print("Do you go through the door on the: right")
    print("Or, do you go through the door on the: left")
    
    door_choice = input("> ")

    if door_choice == "right":
        print("You enter a dark room with only one candle for light and a single door ahead")
        print("Do you open the: door") 
        print("or put out the: candle")
        teleport = random.choice([False, True])

    while True:
        room_choice = input("> ").strip().lower()

        if room_choice == "door" and not teleport:
            dead("You are truly unlucky...")
        elif room_choice == "door" and teleport:
            print("This place looks new")
            teleport = True
            Barrowmaze()
        elif room_choice == "candle" and not teleport:
            dead("Should have stayed outside...")
        elif room_choice == "candle" and teleport:
            print("You feel like you have been here before")
            teleport = False
            Stonehell_Dungeon()
        else:
            break

    if door_choice == "left":
        print("You come to a small round hobbit-like door")
        print("Upon entry you see a single monolith in the center of the room")
        print("Do you approach the: monolith")
        print("Or, do you take a chance at looking: around")
        flooding_room = random.choice([False, True])

    while True:
        room_choice = input("> ").strip().lower()

        if room_choice == "monolith" and not flooding_room:
            dead("The monolith glow bright red and fills the room with water, should have learned to swim...")
        elif room_choice == "monolith" and flooding_room:
            print("When you touch the monolith you see the room begin to swirl in space and time")
            flooding_room = True
            Barrowmaze()
        elif room_choice == "around" and not flooding_room:
            dead("As you look around you stumble over a cobblestone and break your neck...")
        elif room_choice == "around" and flooding_room:
            print("Your curiosity has saved you, as you find a another hobbit-like door in dark corner")
            flooding_room = False
            Barrowmaze()
        else:
            break


def Barrowmaze():
    print("You made it to BarrowMaze\n")
    print("You enter through a large stone archway")
    print("The hall is lit by torches on either side of the walls.")
    print("There seems to be no end to this maze\n")
    print("To your left there appears to be a long hall with a large iron gate")
    print("To your right there is a narrow corridor that leads into darkness\n")
    print("Will it be to the left down the long: hall")
    print("Or, to the right into: darkness")

    corridor_choice = input("> ")

    if corridor_choice == "hall":
        print("You approach the large iron gate")
        print("As you reach for the handle you hear a voice")
        print("You hear: What gets bigger the more you take away?\n")
        riddle_door = True

    while True:
        choice = input("> ").strip().lower()

        if choice == "hole" and riddle_door:
            print("The gate opens, revealing the golden statue....You Win!")
            exit(0)
        else:
            print("The gate remains closed. The voice chuckles.")
            print("Voice: Incorrect!")
            Rappan_Athuk()
            break

    if corridor_choice == "darkness":
        print("You venture into the narrow corridor")
        print("After walking some distance you come across a large mirror hanging on the wall")
        print("Do you look into the: mirror")
        print("Or, keep: moving")
        mirror = random.choice([False, True])

    while True:
        choice = input("> ").strip().lower()

        if choice == "mirror" and not mirror:
            print("You see yourself and feel compelled to reach out and touch the mirror")
            print("As you touch the icy cold mirror you feel cold and dizzy")
            print("Suddenly you are sucked into the mirror and everything goes black")
            mirror = True
            Tegel_Manor()
        elif choice == "moving" and mirror:
            dead("You wonder aimlessly into abyss and starve to death")


def dead(why):
    print(why,"Game Over")
    exit(0)

    #define all paths a character can take
def start():
    print("You have three paths in front of you. ")
    print("Do you take the middle path: 1")
    print("Do you take the right path: 2")
    print("Or, do you take the left path: 3")

    choice = input("> ")

    if choice == "1":
        Rappan_Athuk()
    elif choice == "2":
        print("You have reached a fork in the road. ")
        print("You may take the path to the: right")
        print("Or, you may take the path to the: left")
    
        sub_choice = input("> ")
    
        if sub_choice == "right":
            Tegel_Manor()
        elif sub_choice == "left":
            Stonehell_Dungeon()
        else:
            print("Hurry up and make a decision. ")    
    elif choice == "3":
        Temple_of_Black_Earth()
    else:
        print("Just go home. ")

    choice = input("> ")

    if choice == "right":
        Tegel_Manor()
    elif choice == "left":
        Stonehell_Dungeon()
    else:
        print("Hurry up and make a decision. ")
start()

