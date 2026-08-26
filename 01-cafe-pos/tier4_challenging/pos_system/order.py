"""
CHALLENGE PART 2 of 4: The Order

See menu.py for an overview of this whole project. Complete menu.py first,
since this file needs it.

YOUR TASK (this file)
----------------------
Build an Order class that stores items WITH QUANTITIES (this is harder
than the tier3 Order class, which only stored a plain list). For example,
if a customer orders 2 coffees and 1 muffin, self.items should end up
looking something like: {"Coffee": 2, "Muffin": 1}
"""

from menu import Menu


class Order:
    """Represents one customer's order, including quantities."""

    def __init__(self, menu: Menu):
        self.items = {}
        self.menu = menu

    def add_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            if self.menu.has_item(item_name):
                self.items[item_name] = quantity
            else:
                print(f"Sorry we do not currently stock {item_name}")

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items and self.items[item_name] <= quantity:
            self.items[item_name] -= quantity
            print(f"Removed {item_name} from your order")
        else:
            print(f"It doesn't look like you have {item_name} in your order")            

    def get_subtotal(self):
        subtotal = 0
        for item in self.items:
            subtotal += self.items[item] * self.menu.get_price(item)
        return subtotal


if __name__ == "__main__":
    menu = Menu()
    order = Order(menu)
    order.add_item("Coffee", 2)
    order.add_item("Muffin", 1)
    order.add_item("Tea", 1)
    print("Order items:", order.items)
    print("Subtotal:", order.get_subtotal())
