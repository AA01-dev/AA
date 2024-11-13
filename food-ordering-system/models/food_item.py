# models/food_item.py
class FoodItem:
    def __init__(self, id, name, price, ingredients):
        self.id = id
        self.name = name
        self.price = price
        self.ingredients = ingredients