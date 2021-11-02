nums = []

for count in range(3):
    num = int(input("Enter a number to add to the list: "))
    nums.append(num)

del_last_num = input("Do you still want the last number saved? [y/n] ").lower()
if del_last_num == 'n':
    nums.pop()

print(nums)