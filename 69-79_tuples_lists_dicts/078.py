tv_show = ["Teen Titans", "Gumball", "Dragonball", "Naruto"]

for show in tv_show:
    print(show)

inp_show = input("Enter another show: ")
show_position = int(input("Enter a position between 0 and 3 for the show: "))

tv_show.insert(show_position, inp_show)
for show in tv_show:
    print(show)