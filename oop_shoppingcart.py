# Object Oriented Shopping Cart:

class Shopping_Cart():

    def __init__(self, capacity, items):
        self.capacity = capacity
        self.items = items

    def showCart(self):
        print("Items in your cart: ")
        if self.items == []:
            print("Your cart is empty.")
        else:
            for item in self.items:
                print(item)

    def addToCart(self):
        goods = input("What would you like to add to your cart? (item, price) ")
        self.items.append(goods)

    def deleteCart(self):
        delete_item = input("What item would you like to remove? ")
        self.items.remove(delete_item)

your_cart = Shopping_Cart(10, [])

# Function to run the Shopping Cart Program:

def shop():
    while True:
        response = input("What would like to do? Add/Show/Delete/Quit")
        
        if response.lower() == 'quit':
            your_cart.showCart()
            print("Thank you for shopping with us!")
            break
        elif response.lower() == "add":
            your_cart.addToCart()
        elif response.lower() == "show":
            your_cart.showCart()
        elif response.lower() == "delete":
            your_cart.deleteCart()
         
shop()  