people_info = {}

for people in range(4):
    name = input("Enter a name of a person: ")
    age = int(input("Enter their age: "))
    shoe_size = int(input("Enter their shoe size: "))
    people_info[name] = {"age":age, "shoe size": shoe_size}

name = input("Enter the name of one of the people: ")
print(f"{name} is {people_info[name]['age']} years old and has a shoe size of {people_info[name]['shoe size']}.")