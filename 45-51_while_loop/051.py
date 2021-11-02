green_bottles = 10

while green_bottles > 0:
    print(
        f"There are {green_bottles} green bottles hanging on the wall, "
        f"{green_bottles} green bottles hanging on the wall, "
        "and if 1 green bottle should accidently fall"
    )

    green_bottles -= 1

    while True:
        answer = int(input("How many green bottles will be hanging on the wall? "))

        if answer != green_bottles:
            print("No, try again")
            continue
        break

    print(f"There will be {green_bottles} green bottles hanging on the wall")

print("There are no more green bottles hanging on the wall.")
