subjects = ["English", "Maths", "Life Science", "Life Orientation", "Afrikaans", "Accounting"]
print(subjects)

dislike = input("Which of the subjects do you not like? ").title()
subjects.remove(dislike)

print(subjects)