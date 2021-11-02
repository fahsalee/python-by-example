from array import *

nums = array('i', [21, 5, 13, 78, 69])
print(nums)

sel_num = int(input("Enter one of the displayed numbers: "))

while sel_num not in nums:
    sel_num = int(input("That number is not in the array. Try again: "))

print(nums.index(sel_num))