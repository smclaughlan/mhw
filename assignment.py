name = input("Enter your name.\n")
amount = input("Enter the amount of sales in numeric digits\n")
amount = int(amount)
if amount <= 4999:
    commission = 0
    print("You did not get above $5000 so you don't get any commission.")
if amount >= 5000 and amount <= 10000:
    commission = format(amount * 0.05, ".2f")
    print("Your commission is", commission)
if amount >= 10001:
    commission = format(amount * 0.075, ".2f")
    print("Your commission is", commission)
print(
    f"Hello, {name}. You made ${amount} in sales, made ${commission} in commission.")
