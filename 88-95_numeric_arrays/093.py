from array import *

nums = array('i', [])

for i in range(5):
    newvalue = int(input("Enter a number: "))
    nums.append(newvalue)

nums = sorted(nums)
print(nums)

rem_num = int(input("Select one of the numbers: "))

if rem_num in nums:
    nums.remove(rem_num)
    nums2 = array('i', [rem_num])
    print(nums)
    print(nums2)
else:
    print("That number is not in the array")