vowels = ('a', 'e', 'i', 'o', 'u')

word = input("Enter a word: ").lower()

if word[0] in vowels:
    p_latin_word = word + 'way'
else:
    p_latin_word = word[1:] + word[0] + 'ay'

print(f"{word} in Pig Latin is {p_latin_word}.".capitalize())