# models/order.py
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