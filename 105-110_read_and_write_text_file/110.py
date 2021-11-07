file = open("Names.txt", "r")
print(file.read())
file.close()

file = open("Names.txt", "r")
exceptname = input("Enter one of the names: ") + "\n"
file2 = open("Names2.txt", "a")
for name in file:
    if name != exceptname:
        file2.write(name)
file2.close()
file.close()