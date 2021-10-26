total = 0

for count in range(0, 5):
    num = int(input("Enter a number: "))
    included = input("Include the number? [y/n] ").lower()
    if included == 'y':
        total += num

print(total)