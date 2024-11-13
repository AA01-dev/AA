class Inventory:
    def __init__(self):
        self.stock = {
            "cheese": 20,
            "bread": 15,
            "lettuce": 10,
            "tomato": 10,
            "pasta": 8,
            "pizza_dough": 5,
            "sauce": 10
        }

    def check_ingredients(self, ingredients):
        for ingredient, qty in ingredients.items():
            if self.stock.get(ingredient, 0) < qty:
                return False
        return True

    def update_inventory(self, ingredients):
        for ingredient, qty in ingredients.items():
            if ingredient in self.stock:
                self.stock[ingredient] -= qty
        print("Inventory updated successfully.")

    def view_inventory(self):
        print("\nInventory Stock:")
        for item, qty in self.stock.items():
            print(f"{item}: {qty} units")
        print()