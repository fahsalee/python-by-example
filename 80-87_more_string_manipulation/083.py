while True:
    word = input("Type in a word in upper case: ")

    if word.isupper() == False:
        print("Try again")
        continue
    break