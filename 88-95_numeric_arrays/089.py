from array import *
import random

randint_array = array('i', [])

for num in range(5):
    randnum = random.randint(1, 100)
    randint_array.append(randnum)

for num in randint_array:
    print(num)