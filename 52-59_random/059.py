import random

colours = ["Green", "Blue", "Red", "Yellow", "Gold"]
chosen_colour = random.choice(colours)

print("   ".join(colours))
answer = input("Pick one of the above colours: ").capitalize()

while answer != chosen_colour:
    if chosen_colour == 'Green':
        print("I bet you are GREEN with envy")
    elif chosen_colour == 'Blue':
        print("You are probably feeling BLUE right now")
    elif chosen_colour == 'Red':
        print("You are probably RED in anger")
    elif chosen_colour == 'Yellow':
        print("If you're not YELLOW you'll try again")
    elif chosen_colour == 'Gold':
        print("Get it right and you might feel a little GOLD")

    answer = input("Guess again: ").capitalize()

print("Well done")