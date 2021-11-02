num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
total = num1 + num2
add = input("Do you want to add another number? [y/n] ").lower()

while add == 'y':
    num = int(input("Enter a number: "))
    total += num
    add = input("Do you want to add another number? [y/n] ").lower()

print(f"The total is {total}.")