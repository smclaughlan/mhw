import random

prices_of_stuff = {
    "chocolate": 2,
    "chips": 2,
    "soda": 1.5,
    "water": 1,
    "lottery ticket": 5,
    "gum": 2,
    "flowers": 7,
    "cigarettes": 10,
    "cake": 4.5,
    "burger": 3.99,
}

codes_of_stuff = {
    "chocolate": 16,
    "chips": 10,
    "soda": 2,
    "water": 4,
    "lottery ticket": 14,
    "gum": 19,
    "flowers": 11,
    "cigarettes": 3,
    "cake": 8,
    "burger": 1,
}

color_prices = {
    "red": 2.5,
    "pink": 3.25,
    "blue": 2.99,
    "purple": 3.99,
}


def format_money(num):
    return format(num, '.2f')


def wheel_one():
    wheel_one = [1, 2, 3, 4, 5]
    return random.choice(wheel_one)


def wheel_two():
    wheel_two = ["red", "blue", "pink", "purple"]
    return random.choice(wheel_two)


items = ["chocolate: $2", "chips: $2"]
userShopping = True
total = 0
shoppingList = []
while userShopping:
    for item in prices_of_stuff:
        print(f"{item}: ${format_money(prices_of_stuff[item])}")
    buyItem = input("which item would you like to buy?\n")
    number_of_items = int(input("How many units?\n"))
    total += prices_of_stuff[buyItem] * number_of_items
    shoppingList.append([buyItem, number_of_items])
    answer = input("Keep shopping?\n")
    if answer.lower() == "no" or answer.lower() == "n" or answer.lower() == "nope":
        userShopping = False

reduced_list = []
spins = 3
keep_playing = True
answer = "yes"
price_result = 0
while spins > 0 and keep_playing:
    answer = input("Do you want to play a game to try to get a discount?\n")
    if answer == "yes":
        wheel_one_res = wheel_one()
        wheel_two_res = wheel_two()
        color_price = color_prices[wheel_two_res]
        print(
            f"We spun both wheels and got code number {wheel_one_res} on the first wheel, the color {wheel_two_res} and the price ${format_money(color_price)} on the second wheel!")
        if wheel_one_res in codes_of_stuff.values():
            original_item = list(
                filter(lambda item: codes_of_stuff[item] == wheel_one_res, codes_of_stuff))[0]
            shopping_list_item_names = [item[0] for item in shoppingList]
            if original_item in shopping_list_item_names:
                original_item_price = prices_of_stuff[original_item]
                if original_item_price > color_price:
                    price_result = color_price
                else:
                    price_result = (original_item_price * .1)
                num_of_units = [item[1]
                                for item in shoppingList if item[0] == original_item][0]
                reduced_list.append(
                    [original_item, original_item_price, price_result, num_of_units])
                print("Here are your price reductions now:")
                for item in reduced_list:
                    print(
                        f"{item[0]} used to be ${format_money(item[1])} but is now ${format_money(item[2])}, for a total of ${format_money(item[2] * item[3])}")
        spins = spins - 1
        print(f"Spins remaining: {spins}")
    else:
        keep_playing = False

total_actual = 0

reduced_list_item_names = [item[0] for item in reduced_list]
shopping_list_filtered = filter(
    lambda item: item[0] not in reduced_list_item_names, shoppingList)

for item in shopping_list_filtered:
    total_actual += prices_of_stuff[item[0]] * item[1]
    print(f"{item[0]} -- {format_money(prices_of_stuff[item[0]] * item[1])}")

total_reduced = 0
total_full = 0
print("Reduced items:")
for item in reduced_list:
    total_reduced += item[2] * item[3]
    total_full += item[1] * item[3]
    #
    print(f"{item[0]} -- {item[2] * item[3]}")

print(
    f"Your total is ${format_money(total_reduced + total_actual)}. You saved ${format_money(total_full - total_reduced)}.")  # yeah something is off
