from array import *

nums = array('i', [2, 5, 3, 5, 6])

print(nums)
ask_val = int(input("Enter one of the numbers displayed: "))

count_val = nums.count(ask_val)
print(f"{ask_val} appears in the list {count_val} time(s).")