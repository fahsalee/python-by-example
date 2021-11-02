import random

num = random.randint(1, 10)

while True:
    user_num = int(input("Enter a number: "))

    if user_num < num:
        print("Too low")
    elif user_num > num:
        print("Too high")
    elif user_num == num:
        break