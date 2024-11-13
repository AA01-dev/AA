# models/kitchen.py
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