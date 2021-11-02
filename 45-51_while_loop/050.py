num = int(input("Enter a number between 10 and 20: "))

while True:
    num = int(input("Enter a number between 10 and 20: "))

    if num < 10:
        print("Too low")
        continue
    if num > 20:
        print("Too high")
        continue
    break

print("Thank you")