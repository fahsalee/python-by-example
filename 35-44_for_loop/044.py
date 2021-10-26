num_of_people = int(input("How many people do you want to invite to the party: "))

if num_of_people < 10:
    print("Who would you like to invite?")
    for person in range(0, num_of_people):
        name = input("Enter their name: ")
        print(f"{name} has been invited")
else:
    print("Too many people")