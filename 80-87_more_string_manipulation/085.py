vowels = ('a', 'e', 'i', 'o', 'u')
name = input("Enter your name: ")

num_of_vowels = 0
for letter in name.lower():
    if letter in vowels:
        num_of_vowels += 1

print(f"There are {num_of_vowels} vowels in your name.")