import time
import random


def print_pause1(string):
    print(string)
    time.sleep(1)


def print_pause(string):
    print(string)
    time.sleep(2)


def loading_screen():
    print_pause("GAME LOADING")
    for n in range(3):
        print_pause1(".")


def intro(coworker):
    loading_screen()
    print_pause("You're the first to walk into the office "
                "on Tuesday morning.")
    print_pause("You sit at your desk, start up your computer, "
                "and begin to scroll through your emails.")
    print_pause("You hear someone else walk in.")
    print_pause(f"You look up to see {coworker} "
                "walk by and you let out a quiet but "
                "pained sigh.")
    print_pause("You turn back to your desk to grab your coffee "
                "mug when you notice it isn't there.")
    print_pause("After some minutes of searching your desk "
                "you realize your mug isn't in the office.")
    print_pause("You decide to search elsewhere.")
    print_pause("Straight ahead is the hallway leading "
                "to the restroom.")
    print_pause("To your right is the break room.")


def office(coworker, items, print_again):
    print_pause("Enter 1 to go to the restroom.")
    print_pause("Enter 2 to check the break room" + print_again[-1] + ".")
    print_pause("What would you like to do?")
    while True:
        first_choice = input("(Please enter 1 or 2.)\n")
        if first_choice == "1":
            restroom(coworker, items, print_again)
            break
        elif first_choice == "2":
            breakroom(coworker, items, print_again)
            break


def restroom(coworker, items, print_again):
    print_pause("You take a quick trip to the restroom.")
    print_pause(f"You open the hallway door to reveal {coworker}.")
    print_pause(f"Enter 1 to ask {coworker} about your missing mug.")
    print_pause("Enter 2 to avoid conversation and walk back to the office.")
    while True:
        second_choice = input("(Please enter 1 or 2.)\n")
        if second_choice == "1":
            ask(coworker, items, print_again)
            break
        elif second_choice == "2":
            leave(coworker, items, print_again)
            break


def breakroom(coworker, items, print_again):
    print_again.append(" again")
    print_pause("You decide to check the break room.")
    if "donut" in items:
        print_pause(f"You open the door to find {coworker} "
                    "frowning at you.")
        print_pause(f'''"The last donut was mine," {coworker} '''
                    '''says. "Give it back or I'm telling Michael."''')
        print_pause("Enter 1 to return the donut.")
        print_pause("Enter 2 to keep the donut.")
        while True:
            third_choice = input("(Please enter 1 or 2.)\n")
            if third_choice == "1":
                return_donut(coworker, items, print_again)
                break
            elif third_choice == "2":
                keep_donut(coworker, items, print_again)
                break
    else:
        items.append("donut")
        print_pause("You look around, but can't find your mug.")
        print_pause("However, you do find a lone donut "
                    "leftover from yesterday's meeting, "
                    "hidden away at the back of the fridge.")
        print_pause("You take the donut and return to the office.")
        office(coworker, items, print_again)


def return_donut(coworker, items, print_again):
    items.remove("donut")
    print_pause(f"You decide that the donut isn't "
                "worth Michael's involvement.")
    print_pause("He's been in a weird mood since Jan dumped him.")
    print_pause("You return the donut and go back to the office.")
    office(coworker, items, print_again)


def keep_donut(coworker, items, print_again):
    print_pause(f"You lie, telling {coworker} that you're unaware "
                "of any such donut.")
    print_pause(f"{coworker} stares at you with what one "
                "could only describe as pure, unyielding hatred.")
    print_pause(f"{coworker} huffs and leaves the break room, "
                "slamming the door on the way out.")
    office(coworker, items, print_again)


def ask(coworker, items, print_again):
    if "donut" in items:
        print_pause("You ask about your missing mug.")
        print_pause(f"{coworker} begins to reply, but then...")
        print_pause(f"...you pull out the donut.")
        print_pause(f"{coworker} pauses, eyes narrowed.")
        print_pause(f"{coworker} walks back into the office, "
                    "then returns with your mug.")
        print_pause("You trade the donut for your mug and walk "
                    "back to your desk, ready to face another day.")
        print_pause("Congratulations! You've won the game!")
        play_again()
    else:
        print_pause(f"You confront {coworker} directly about "
                    "your missing mug.")
        print_pause('''"I have no idea what you're talking '''
                    f'''about," {coworker} responds. "I'll ask '''
                    '''Michael if he's seen it."''')
        print_pause(f"Before you have a chance to reply, {coworker} "
                    "turns suddenly and walks out the door.")
        print_pause("You walk back to your desk, only to run into Michael.")
        print_pause(f'''"{coworker} told me about your mug! I'll help '''
                    '''you find it! By the way, I've been meaning to '''
                    '''bounce some ideas off you about this '''
                    '''year's Dundies..."''')
        print_pause("You sigh again. It's going to be a long day.")
        print_pause("You are trapped in a pointless conversation "
                    "with Michael! You lose!")
        play_again()


def leave(coworker, items, print_again):
    print_pause("You turn and speedwalk back to the office.")
    office(coworker, items, print_again)


def play_again():
    print_pause("GAME OVER")
    while True:
        answer = input("Would you like to play again? (y/n)\n").lower()
        if answer == "y":
            print_pause("Great! Restarting game...")
            main()
            break
        elif answer == "n":
            print_pause("Thanks for playing!")
            break


def main():
    coworkers = ["Dwight", "Oscar", "Angela", "Meredith", "Phyllis",
                 "Andy"]
    coworker = random.choice(coworkers)
    items = []
    print_again = [""]
    intro(coworker)
    office(coworker, items, print_again)


main()

