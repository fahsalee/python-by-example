fav_foods = {}

food = input("Enter a favourite food: ")
fav_foods[1] = food

food = input("Enter a second favourite food: ")
fav_foods[2] = food

food = input("Enter a third favourite food: ")
fav_foods[3] = food

food = input("Enter a fourth favourite food: ")
fav_foods[4] = food

print(fav_foods)

rid_food = int(input("Which item number do you want to remove? "))
fav_foods.pop(rid_food)

print(sorted(fav_foods.values()))