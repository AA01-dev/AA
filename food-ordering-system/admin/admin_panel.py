# admin/admin_panel.py
class AdminPanel:
    def __init__(self, menu, orders, inventory, kitchen, delivery):
        self.menu = menu
        self.orders = orders
        self.inventory = inventory
        self.kitchen = kitchen
        self.delivery = delivery

    def display_admin_menu(self):
        print("\nAdmin Panel:")
        print("1. View Orders")
        print("2. Update Order Status")
        print("3. Manage Inventory")
        print("4. Prepare Order in Kitchen")
        print("5. Assign Delivery")
        print("6. Exit")

    def view_orders(self):
        if not self.orders:
            print("No orders available.")
            return
        for order in self.orders:
            order.view_order()

    def update_order_status(self, order_id, status):
        for order in self.orders:
            if order.order_id == order_id:
                order.status = status
                print(f"Order {order_id} status updated to '{status}'")
                return
        print("Order not found.")

    def manage_inventory(self):
        self.inventory.view_inventory()

    def assign_delivery(self, order_id):
        for order in self.orders:
            if order.order_id == order_id and order.status == "Prepared":
                self.delivery.assign_delivery(order)
                return
        print("Order not found or not ready for delivery.")