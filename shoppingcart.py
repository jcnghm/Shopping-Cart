#  Building a Python shopping cart
#  Dictionary Exercise

def shoppingCart():
    cart = {}
    while True:
        command = input("What would you like to do? Add/Show/Delete/Quit")
        if command.lower() == "add":
            item = input("What would you like to add to you cart? ")
            price = input("What is the price of that item? ")
            cart[item] = price
            continue
        if command.lower() == "show":
            print(cart)
            continue
        if command.lower() == "delete":
            item = input("Indicate which item you'd like to delete. ")
            if item not in cart:
                print("You don't have any of that item in your cart!")
                continue
            del cart[item]
            print(cart)
            continue
        if command.lower() == "quit":
            print("Here is your completed cart: ")
            print(cart)
            break

shoppingCart()
