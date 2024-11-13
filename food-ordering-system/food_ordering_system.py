# food_ordering_system.py
from models.menu import Menu
from models.cart import Cart
from models.inventory import Inventory
from models.order import Order
from models.kitchen import Kitchen
from models.delivery import Delivery
from admin.admin_panel import AdminPanel

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