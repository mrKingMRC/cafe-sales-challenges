MENU = {
    "Coffee": 4.50,
    "Tea": 3.50,
    "Muffin": 5.00,
    "Toastie": 6.50,
    "Hot Chocolate": 4.00,
}
class Order:
    """Represents one customer's order at The Trendiest Café."""

    def __init__(self):
        self.items = []


    def add_item(self, item_name):
        if item_name in MENU:
            self.items.append(item_name)
            print(f"Added {item_name} to your order!")
        else:
            print("Not in this store bucko")

    def remove_item(self, item_name):
        if item_name in self.items:
            self.items.remove(item_name)
            print(f"Removed {item_name} from your order!")
        else:
            print(f"You have not ordered {item_name}")

    def get_total(self):
        totalprice = 0
        for item_name in self.items:
            totalprice += MENU[item_name]
        return totalprice



if __name__ == "__main__":
    my_order = Order()
    my_order.add_item("Coffee")
    my_order.add_item("Muffin")
    my_order.add_item("Toastie")
    my_order.add_item("Tea")
    my_order.remove_item("Tea")

    print(f"Current order: {my_order.items}")
    print(f"Order total: ${my_order.get_total()}")
