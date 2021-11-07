simple_2dlist = [[2, 5, 8],[3, 7, 4],[1, 6, 9],[4, 2, 0]]

row = int(input("Select a row from 0 to 3: "))
print(simple_2dlist[row])

newvalue = int(input("Enter a new value to add to the row: "))
simple_2dlist[row].append(newvalue)
print(simple_2dlist[row])