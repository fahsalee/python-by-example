count = 0
invite = 'y'

while invite == 'y':
    name = input("Enter the name of someone to invite to the party: ")
    print(f"{name} has been invited.")
    count += 1
    invite = input("Do you want to invite someone else? [y/n] ").lower()

print(f"You invited {count} people to the party.")