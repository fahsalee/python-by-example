total_bill = int(input("Please enter the total price of the bill: "))
diners = int(input("Please enter how many people there are: "))
divided_bill = total_bill/diners

print(f"Each person must pay R{divided_bill}")