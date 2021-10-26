fname = input("Enter your first name: ")

if len(fname) < 5:
    surname = input("Enter your surname: ")
    name = f"{fname}{surname}".upper()
    print(name)
else:
    print(fname.lower())