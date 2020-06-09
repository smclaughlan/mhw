print(["cookies, $3", "milk, $3", "juice,  $3",
       "soap, $2", "detergent, $5", "shampoo, $4"])
thislist = {
    "cookies": 3,
    "soap": 2,
    "milk": 3,
    "detergent": 5,
    "juice": 3,
    "shampoo": 4,
}
is_food = {
    "soap": False,
    "cookies": True,
    "milk": True,
    "detergent": False,
    "juice": True,
    "shampoo": False
}


def makeReceipt():
    receipt = "Receipt\n"
    for item in shoppingList:
        receipt += f"{item[0]} {item[1]} {format(thislist[item[0]] * item[1], '.2f')}\n"
    print(receipt)


def calcTax():
    tax = 0
    taxable = 0

    for item in shoppingList:
        if item[2] == False:
            taxable += (thislist[item[0]] * item[1])
    tax = taxable * 0.13
    print(f"Tax: {format(tax, '.2f')} Grand Total: {format(total + tax, '.2f')}")


userShopping = True
total = 0
shoppingList = []
while userShopping:
    buyItem = input("which object?")

    if buyItem in is_food:
        number_of_items = int(input("How many units?"))
        total += thislist[buyItem] * number_of_items

        shoppingList.append([buyItem, number_of_items, is_food[buyItem]])

        # [["soap", 2, False], ["cookies", 1, True]]
    answer = input("Keep shopping?")
    if answer.lower() == "no" or answer.lower() == "n" or answer.lower() == "nope":
        userShopping = False


makeReceipt()
calcTax()
