countries = ("South Africa", "India", "Turkey", "Japan", "Russia")
print(countries)

country = input("Enter one of the displayed countries: ").title()
print(f"The index of {country} is {countries.index(country)}.")