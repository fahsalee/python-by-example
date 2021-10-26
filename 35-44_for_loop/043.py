direction = input("Do you want to count up or down? ").lower()

if direction == 'up':
    num = int(input("Enter the top number: "))
    for count in range(1, num + 1):
        print(count)
elif direction == 'down':
    num = int(input("Enter a number below 20: "))
    for count in range(20, num - 1, -1):
        print(count)
else:
    print("I don't understand.")