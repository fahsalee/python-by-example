days = int(input("Enter number of days: "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(
    f"{hours} hours in {days} day(s)"
    f"\n{minutes} minutes in {days} day(s)"
    f"\n{seconds} seconds in {days} day(s)"
)