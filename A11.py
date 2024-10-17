# Menu stored as a dictionary (food item: price)
menu_items = {
    'Burger': 5.99,
    'Pizza': 8.99,
    'Fries': 2.99,
    'Salad': 4.50,
    'Soda': 1.99,
    'Coffee': 2.50
}

# Customer's order stored as a list of tuples (food item, price)
customer_order = []

# Function to display available menu items
def show_menu():
    print("\n--- QuickBite Menu ---")
    for dish, cost in menu_items.items():
        print(f"{dish}: ${cost:.2f}")

# Function to add a menu item to the order
def add_to_order():
    show_menu()
    selected_item = input("\nSelect an item to add (or type 'q' to exit): ").title()
    
    if selected_item == 'Q':
        return
    elif selected_item in menu_items:
        customer_order.append((selected_item, menu_items[selected_item]))
        print(f"{selected_item} has been added to your order.")
    else:
        print("Sorry, that item isn't available.")

# Function to view current order and calculate total cost
def view_current_order():
    if not customer_order:
        print("\nYour order is currently empty.")
        return
    
    print("\n--- Your Current Order ---")
    total_cost = sum(cost for _, cost in customer_order)
    for item, cost in customer_order:
        print(f"{item}: ${cost:.2f}")
    print(f"\nTotal: ${total_cost:.2f}")

# Function to remove an item from the current order
def remove_from_order():
    if not customer_order:
        print("\nYour order is empty, nothing to remove.")
        return
    
    view_current_order()
    remove_item = input("\nWhich item would you like to remove? ").title()
    for i, (item, _) in enumerate(customer_order):
        if item == remove_item:
            customer_order.pop(i)
            print(f"{remove_item} has been removed from your order.")
            return
    print(f"{remove_item} is not in your order.")

# Function to checkout and finalize the order
def finalize_order():
    if not customer_order:
        print("\nYou don't have any items in your order.")
        return

    view_current_order()
    confirm = input("\nWould you like to confirm your order? (y/n): ").lower()
    if confirm == 'y':
        print("\nThank you for ordering with QuickBite! Your order has been successfully placed.")
        customer_order.clear()  # Clear the order after confirmation
    else:
        print("Order was not confirmed. Returning to menu.")

# Main function to run the system
def quickbite_system():
    while True:
        print("\n--- QuickBite Ordering System ---")
        print("1. View Menu")
        print("2. Add Item to Order")
        print("3. View Current Order")
        print("4. Remove Item from Order")
        print("5. Checkout and Exit")
        
        user_choice = input("Please select an option (1-5): ")
        
        if user_choice == '1':
            show_menu()
        elif user_choice == '2':
            add_to_order()
        elif user_choice == '3':
            view_current_order()
        elif user_choice == '4':
            remove_from_order()
        elif user_choice == '5':
            finalize_order()
            break
        else:
            print("Invalid option. Please try again.")

# Start the system when the program runs
if __name__ == "__main__":
    quickbite_system()