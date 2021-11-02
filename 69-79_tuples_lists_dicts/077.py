name1 = input("Enter the name of someone you want to invite to the party: ")
name2 = input("Enter the name of someone else you want to invite to the party: ")
name3 = input("Enter the name of someone else you want to invite to the party: ")
invited = [name1, name2, name3]

invite_more = input("Do you want to invite someone else? [yes/no] ").lower()

if invite_more == 'yes':
    while True:
        name = input("Enter the name of who you want to invite: ")
        invited.append(name)

        invite_more = input("Do you want to invite someone else? [yes/no] ").lower()
        
        if invite_more == 'no':
            break

print(f"You invited {len(invited)} people to the party.")

print(invited)

pick_name = input("Enter one of the names on the list: ")
print(f"{pick_name} is in position {invited.index(pick_name)} on the list.")

uninvite = input(f"Do you still want {pick_name} to come to the party? [yes/no] ")

if uninvite == 'no':
    invited.remove(pick_name)
    print(invited)