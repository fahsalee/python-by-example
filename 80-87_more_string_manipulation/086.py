password = input("Enter a new password:\n")
confirm_password = input("Enter your password again:\n")

if confirm_password == password:
    print("Thank you")
elif confirm_password.lower() == password.lower():
    print("They must be in the same case")
else:
    print("Incorrect")