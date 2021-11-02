countries = ("South Africa", "India", "Turkey", "Japan", "Russia")
print(countries)

country = input("Enter one of the displayed countries: ").title()
print(f"The index of {country} is {countries.index(country)}.")

position = int(input("Enter a number between 0 and 4: "))
print(countries[position])