num = int(input("Enter a number between 1 and 12: "))

for times in range(1, 13):
    answer = num * times
    print(f"{num} x {times} = {answer}")