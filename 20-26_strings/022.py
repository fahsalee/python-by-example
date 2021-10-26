first_name = input("Enter your first name in lower case: ")
surname = input("Enter your surname in lower case: ")

first_name = first_name.title()
surname = surname.title()
name = f"{first_name} {surname}"

print(name)