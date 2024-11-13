# models/cart.py
class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, food_item):
        self.items.append(food_item)
        print(f"Added {food_item.name} to the cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        print("\nCart Items:")
        total = 0
        for item in self.items:
            print(f"{item.name} - ${item.price:.2f}")
            total += item.price
        print(f"Total: ${total:.2f}\n")

    def clear_cart(self):
        self.items = []