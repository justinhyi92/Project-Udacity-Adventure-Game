import time
import random

list = ["Hades has released Cerberus on you and has eaten you\n", "Hades has overrun Olympus due to your idiocy.\n", "The Ice Titan has frozen you to death.\n", "You are blown off of Olympus by the Wind Titan.\n", "The Fire Titan has melted you.\n", "Hades has called upon Paris Hilton to bore you to death.", "Hades sends Medusa to turn you to stone."]
death = random.choice(list)

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def valid_input(prompt, option1, option2, option3):
    while True:
        choice = input(prompt).lower()
        if option1 in choice:
            return choice
        elif option2 in choice:
            return choice
        elif option3 in choice:
            return choice
        else:
            print_pause("Please choose a number: 1.Hephaestus, 2.Hermes, 3.Zeus,")

def again_input(prompt, y, n):
    while True:
        choice = input(prompt).lower()
        if y in choice:
            return choice
        elif n in choice:
            return choice
        else:
            print_pause("Please press 'y' or 'n'")

def intro():
    print_pause("Welcome, Guardian, to the Kingdom of the Olympus.")
    print_pause("We are in need of your assistance.")
    print_pause("Hades, is preparing an attack to overrule the Kingdom.")
    name = input("What is your name Guardian? ")
    time.sleep(2)
    print("\nGuardian", name, "let us prepare for battle." )
    time.sleep(2)
    print_pause("Zeus is in need of his lightning bolts.")
    print_pause("Go! Before Hades and his minions arrives!\n")

def choose_god(items):
    print_pause("You have three choices of whom to go to.")
    print("Enter 1 to go see Hephaestus.")
    print("Enter 2 to go see Hermes.")
    print("Enter 3 to go see Zeus")
    number = valid_input("Please enter whom you would like to go to. ", "1", "2", "3")
    if number == '1':
        hephaestus(items)
    elif number == '2':
        hermes(items)
    elif number == '3':
        zeus(items)
    print_pause("Where would you like to go next?\n")

def hephaestus(items):
    print_pause("\nYou've walked into the Forge of Hephaestus.")
    if "lightning bolts" in items:
        print_pause("You idiot! What are you doing back here? We're doomed!")
        print_pause(death)
        play_again()
    else:
        print_pause("Hephaestus yells, 'Quickly, take these lightning bolts to Zeus!'")
        print_pause("You have obtained the mighty 'Lightning Bolts'!\n")
        items.append("lightning bolts")
    choose_god(items)

def hermes(items):
    print_pause("\nYou see the God of Travel Hermes.")
    if "winged boots" in items:
        print_pause("You've wasted too much time here! Hades is here now!")
        print_pause(death)
        play_again()
    else:
        print_pause("Hermes comes to you.")
        if "lightning bolts" in items:
            print_pause("He sees that you have received the Lightning Bolts from Hephaestus.")
            print_pause("'Good! Take these boots and hurry with those lightning bolts to Zeus!'")
            print_pause("You have obtained, 'Winged Boots of Travel'.\n")
            items.append("winged boots")
        else:
            print_pause("What are you doing here empyty-handed? You have doomed us!")
            print_pause(death)
            play_again()
    choose_god(items)

def zeus(items):
    print_pause("\nYou've arrived at the top of Olympus")
    print_pause("Zeus is standing upon the clouds, awaiting your arrival.")
    if "lightning bolts" in items:
        print_pause("Zeus sees you with his mighty Lightning bolts.")
        if "winged boots" in items:
            print_pause("Zeus exclaims 'Good! You've made it in time!'")
            print_pause("With Zeus's might Lightning Bolts in hand, Hades and his minions are struck down off of Olympus.\n")
            print_pause("Congratulatons Guardian! You are the savior of Olympus!")
            print_pause("Zeus, welcomes you as a god on Olympus!\n")
            play_again()
        else:
            print_pause(death)
            play_again()
    else:
        print_pause("\nZeus yells, 'Where are my Lightning bolts?!'")
        print_pause("Without his lightning bolts, Zeus cannot stop Hades.")
        print_pause(death)
        play_again()


def play_again():
    print_pause("GAME OVER")
    play = again_input("Would you like to play again? Please say 'y' or 'n'.\n", 'y', 'n')
    if play == 'n':
        print_pause("Thanks for playing Guardian\n")
    elif play == 'y':
        print_pause("Let's kick some butt!\n")
        play_game()

def play_game():
    items = []
    intro()
    choose_god(items)
    play_again()

play_game()
