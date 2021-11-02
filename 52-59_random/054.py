import random

coin = random.choice(['h', 't'])

guess = input("Heads or tails? [h/t] ").lower()

if guess == coin:
    print("You win")
else:
    print("Bad luck")

if coin == 'h':
    print("It was heads")
else:
    print("It was tails")