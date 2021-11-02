from array import *

nums = array('f',[15.71, 21.21, 66.69, 18.19, 76.67])

num = int(input("Enter a number between 2 and 5: "))

while num < 2 or num > 5:
    print("Number not within the given range. Try again")
    num = int(input("Enter a number between 2 and 5: "))

for value in nums:
    answer = value/num
    print(round(answer, 2))