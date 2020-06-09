# notes

# get input from user that will be saved as a string
# amount = input("Enter an amount: ")
# get input but let the user enter it on a new line. \n is the new line character
# amount = input("Enter an amount: \n")
# get input and immediately convert it to an int
amount = int(input("Enter an amount: \n"))

amount = int(amount)  # if we didn't already convert to int, we could do it now

if amount > 20:
    print("The amount is greater than 20")
