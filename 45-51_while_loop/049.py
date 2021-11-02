compnum = 50

guess = int(input("Guess the number: "))
count = 1
while guess != compnum:
    if guess < compnum:
        print("Too low")
    if guess > compnum:
        print("Too high")
    
    count += 1
    guess = int(input("Guess again: "))

print(f"Well done, you took {count} attempts.")