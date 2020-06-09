name = input("Enter your name.\n")
# important note, doing the int() here to get rid of it everywhere else! saves some typing
amount = int(input("Enter the amount of sales in numeric digits\n"))
if amount <= 4999:
    commission = 0
    print("You did not get above $5000 so you don't get any commission")
if amount >= 5000 and amount <= 10000:
    commission = amount * 0.05
    print(f"Your commission is {commission}")
if amount >= 10001:
    commission = amount * 0.075
    print(f"Your commission is {commission}")
print(f"Hello, {name}. You made {amount} sales, with {commission} commission.")

#
#
