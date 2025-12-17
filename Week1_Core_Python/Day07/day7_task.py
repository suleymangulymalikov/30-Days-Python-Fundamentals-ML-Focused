class ShoppingCart:
    
    def __init__(self):
        self.cart = dict()

    def add(self, item, quantity):
        self.cart[item] = quantity
        return {item : quantity}

    def remove(self, item):
        self.cart.pop(item)
        return {item}

    def update(self, item, new_quantity):
        self.cart[item] = new_quantity
        return {item: new_quantity}
    
    def products(self):
        return self.cart

if __name__ == "__main__":
    print("Day 7 Task")

    cart = ShoppingCart()

    print(f"Empty cart created {cart}")

    print(f"Adding products: {cart.add('apple', 2)}")
    print(f"Adding products: {cart.add('cherry', 6)}")
    print(f"Adding products: {cart.add('banana', 5)}")

    print(f"Removing product: {cart.remove('banana')}")

    print(f"Updating product: {cart.update('cherry', 10)}")

    print(f"All products: {cart.products()}")

