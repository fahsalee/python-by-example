name = input("Enter your name: ")
num = int(input("Enter a number: "))

if num < 10:
    for count in range(0, num):
        print(name)
else:
    for count in range(0, 3):
        print("Too high")