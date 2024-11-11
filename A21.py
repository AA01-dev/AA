class FoodItem:
    def __init__(self, id, name, price, ingredients):
        self.id = id
        self.name = name
        self.price = price
        self.ingredients = ingredients

class Inventory:
    def __init__(self):
        # Hardcoded inventory items
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

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
        self.status = "Pending"
        self.delivery_status = "Not Assigned"

    def view_order(self):
        print(f"\nOrder ID: {self.order_id}")
        total = 0
        for item in self.items:
            print(f"{item.name} - ${item.price:.2f}")
            total += item.price
        print(f"Total: ${total:.2f}")
        print(f"Status: {self.status}")
        print(f"Delivery Status: {self.delivery_status}\n")

class Delivery:
    def __init__(self):
        self.delivery_personnel = ["Alice", "Bob"]
        self.orders = []

    def assign_delivery(self, order):
        if not self.delivery_personnel:
            print("No delivery personnel available.")
            return False
        order.delivery_status = f"Assigned to {self.delivery_personnel[0]}"
        self.orders.append(order)
        print(f"Order {order.order_id} assigned to {self.delivery_personnel[0]}")
        return True

    def update_delivery_status(self, order_id, status):
        for order in self.orders:
            if order.order_id == order_id:
                order.delivery_status = status
                print(f"Order {order_id} delivery status updated to '{status}'")
                return
        print("Order not found.")

class Kitchen:
    def __init__(self):
        self.orders_queue = []

    def add_order(self, order):
        self.orders_queue.append(order)
        print(f"Order {order.order_id} added to the kitchen queue.")

    def prepare_order(self):
        if not self.orders_queue:
            print("No orders to prepare.")
            return
        order = self.orders_queue.pop(0)
        order.status = "Prepared"
        print(f"Order {order.order_id} has been prepared and is ready for delivery.")

class AdminPanel:
    def __init__(self, menu, orders, inventory, kitchen, delivery):
        self.menu = menu
        self.orders = orders
        self.inventory = inventory
        self.kitchen = kitchen
        self.delivery = delivery

    def view_orders(self):
        if not self.orders:
            print("No orders have been placed yet.")
            return
        print("\nAll Orders:")
        for order in self.orders:
            order.view_order()

    def update_order_status(self, order_id, status):
        for order in self.orders:
            if order.order_id == order_id:
                order.status = status
                print(f"Order {order_id} status updated to '{status}'.")
                return
        print("Order not found.")

    def manage_inventory(self):
        self.inventory.view_inventory()

    def assign_delivery(self, order_id):
        for order in self.orders:
            if order.order_id == order_id and order.status == "Prepared":
                self.delivery.assign_delivery(order)
                return
        print("Order not ready for delivery or not found.")

    def display_admin_menu(self):
        print("\nAdmin Panel:")
        print("1. View Orders")
        print("2. Update Order Status")
        print("3. Manage Inventory")
        print("4. Prepare Order in Kitchen")
        print("5. Assign Delivery")
        print("6. Exit Admin Panel")

class FoodOrderingSystem:
    def __init__(self):
        self.menu = Menu()
        self.cart = Cart()
        self.orders = []
        self.inventory = Inventory()
        self.kitchen = Kitchen()
        self.delivery = Delivery()
        self.order_id_counter = 1
        self.admin_panel = AdminPanel(self.menu, self.orders, self.inventory, self.kitchen, self.delivery)

    def customer_menu(self):
        while True:
            print("\nCustomer Menu:")
            print("1. View Menu")
            print("2. Add Item to Cart")
            print("3. View Cart")
            print("4. Place Order")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.menu.display_menu()
            elif choice == "2":
                self.menu.display_menu()
                item_id = int(input("Enter item number to add to cart: "))
                item = self.menu.get_item(item_id)
                if item and self.inventory.check_ingredients(item.ingredients):
                    self.cart.add_to_cart(item)
                else:
                    print("Item unavailable due to low inventory.")
            elif choice == "3":
                self.cart.view_cart()
            elif choice == "4":
                if not self.cart.items:
                    print("Your cart is empty! Add items to place an order.")
                else:
                    self.place_order()
            elif choice == "5":
                print("Exiting Customer Menu.")
                break
            else:
                print("Invalid option. Please try again.")

    def place_order(self):
        new_order = Order(self.order_id_counter, list(self.cart.items))
        self.orders.append(new_order)
        self.inventory.update_inventory(
            {ingredient: qty for item in new_order.items for ingredient, qty in item.ingredients.items()}
        )
        print(f"Order placed successfully with Order ID: {self.order_id_counter}")
        self.kitchen.add_order(new_order)
        self.order_id_counter += 1
        self.cart.clear_cart()

    def admin_menu(self):
        while True:
            self.admin_panel.display_admin_menu()
            choice = input("Choose an option: ")

            if choice == "1":
                self.admin_panel.view_orders()
            elif choice == "2":
                order_id = int(input("Enter Order ID to update: "))
                status = input("Enter new status (Pending, Confirmed, Delivered): ")
                self.admin_panel.update_order_status(order_id, status)
            elif choice == "3":
                self.admin_panel.manage_inventory()
            elif choice == "4":
                self.kitchen.prepare_order()
            elif choice == "5":
                order_id = int(input("Enter Order ID to assign delivery: "))
                self.admin_panel.assign_delivery(order_id)
            elif choice == "6":
                print("Exiting Admin Panel.")
                break
            else:
                print("Invalid option. Please try again.")

    def start(self):
        while True:
            print("\nWelcome to the Online Food Ordering System!")
            print("1. Customer Menu")
            print("2. Admin Menu")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.customer_menu()
            elif choice == "2":
                self.admin_menu()
            elif choice == "3":
                print("Exiting System. Thank you!")
                break
            else:
                print("Invalid option. Please try again.")

# Run the system
food_ordering_system = FoodOrderingSystem()
food_ordering_system.start()