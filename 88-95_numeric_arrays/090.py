from array import *

nums = array('i', [])

while len(nums) < 5:
    newval = int(input("Enter a number: "))
    if newval < 10 or newval > 20:
        print("Outside the range")
        continue

    nums.append(newval)

print("Thank you")
for value in nums:
    print(value)