num_list = [7132, 1749, 6669, 8642]

for number in num_list:
    print(number)

unum = int(input("Enter a three-digit number: "))

if unum in num_list:
    print(f"{unum} is in position {num_list.index(unum)}")
else:
    print("That is not in the list.")