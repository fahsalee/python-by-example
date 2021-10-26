shape = int(input(
    "1) Square\n"
    "2) Triangle\n\n"
    "Enter a number: "
))

if shape == 1:
    length = float(input("Enter the length of one side: "))
    area = length * length
    print(f"The area is {area}.")
elif shape == 2:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = (base/2) * height
    print(f"The area is {area}.")
else:
    print(f"Error. {shape} is not one of the options.")