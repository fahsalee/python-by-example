import random

num = random.randint(1, 5)

guess = int(input("Guess the number: "))

if guess == num:
    print("Well done")
else:
    if guess < num:
        print("Too low")
    else:
        print("Too high")

    guess = int(input("Guess again: "))

    if guess == num:
        print("Correct")
    else:
        print("You lose")