simple_2dlist = [[2, 5, 8],[3, 7, 4],[1, 6, 9],[4, 2, 0]]

row = int(input("Select a row from 0 to 3: "))
print(simple_2dlist[row])

col = int(input("Select a column from 0 to 2: "))
print(simple_2dlist[row][col])

change = input("Do you want to change the value? [y/n] ").lower()
if change == 'y':
    newvalue = int(input("Enter a new value: "))
    simple_2dlist[row][col] = newvalue

print(simple_2dlist[row])