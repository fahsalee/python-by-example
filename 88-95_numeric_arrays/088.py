from array import *

nums = array('i', [])

for num in range(5):
    new_value = int(input("Enter a number: "))
    nums.append(new_value)

nums = sorted(nums)
nums.reverse()
print(nums)