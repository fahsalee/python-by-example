ask_user = input(
    "1) Create a new file\n" +
    "2) Display the file\n" +
    "3) Add a new item to the file\n" +
    "Make a selection 1, 2 or 3: "
)

if ask_user == '1':
    file = open("Subject.txt", "w")
    file.write(input("Enter a school subject: "))
    file.close()
    
elif ask_user == '2':
    file = open("Subject.txt", "r")
    print(file.read())
    file.close()

elif ask_user == '3':
    file = open("Subject.txt", "a")
    file.write(f"\n{input('Enter another school subject: ')}")
    file.close()
    file = open("Subject.txt", "r")
    print(file.read())

else:
    print(f"{ask_user} is not a valid option")