from array import *
import random

array1 = array('i', [])
array2 = array('i', [])

for value in range(3):
    newvalue = int(input("Enter a number: "))
    array1.append(newvalue)

for value in range(5):
    newvalue = random.randint(1, 100)
    array2.append(newvalue)
    
array1.extend(array2)
array1 = sorted(array1)

for value in array1:
    print(value)