file = open("Names.txt", "a")

file.write(input("Enter a new name: ") + "\n")
file.close()

file = open("Names.txt", "r")
print(file.read())
file.close()