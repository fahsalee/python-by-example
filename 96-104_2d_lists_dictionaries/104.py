people_info = {}

for people in range(4):
    name = input("Enter a name of a person: ")
    age = int(input("Enter their age: "))
    shoe_size = int(input("Enter their shoe size: "))
    people_info[name] = {"age":age, "shoe size": shoe_size}

rem_person = input("Who do you want to remove from the list? ")
del people_info[rem_person]

for person in people_info:
    print(person, people_info[person]["age"], people_info[person]["shoe size"])