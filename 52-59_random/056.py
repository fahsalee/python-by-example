import random

num = random.randint(1, 10)

while True:
    user_num = int(input("Enter a number: "))

    if user_num == num:
        break