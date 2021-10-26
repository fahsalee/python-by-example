is_raining = input("Is it raining? ").lower()

if is_raining == 'yes':
    is_windy = input("Is it windy? ").lower()
    if is_windy == 'yes':
        print("It is too windy for an umbrella.")
    else:
        print("Take an umbrella.")
else:
    print("Enjoy your day.")