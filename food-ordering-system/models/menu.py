from .food_item import FoodItem

class Menu:
    def __init__(self):
        self.items = [
            FoodItem(1, "Pizza", 12.99, {"cheese": 1, "pizza_dough": 1, "sauce": 1}),
            FoodItem(2, "Burger", 8.99, {"bread": 1, "lettuce": 1, "tomato": 1}),
            FoodItem(3, "Pasta", 10.49, {"pasta": 1, "sauce": 1, "cheese": 1}),
            FoodItem(4, "Salad", 6.99, {"lettuce": 2, "tomato": 1})
        ]

    def display_menu(self):
        print("\nMenu:")
        for item in self.items:
            print(f"{item.id}. {item.name} - ${item.price:.2f}")

    def get_item(self, item_id):
        for item in self.items:
            if item.id == item_id:
                return item
        return None