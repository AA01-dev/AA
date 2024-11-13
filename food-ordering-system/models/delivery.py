# models/delivery.py
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