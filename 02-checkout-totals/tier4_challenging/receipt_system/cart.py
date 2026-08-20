"""
CHALLENGE PART 1 of 4: The Cart

This project (receipt_system) is split across several files that work
together:
    menu_data.json    - the raw menu data (already provided, don't edit)
    cart.py           - (this file) holds items + quantities for one order
    checkout.py       - applies discounts and GST, produces a receipt string
    main.py           - runs the whole program
    test_receipt_system.py - automated checks for your code

Work through them in that order. Run `pytest` at any point to see which
parts are passing.

YOUR TASK (this file)
----------------------
Complete the Cart class so it can hold menu items with quantities, and
report on what's in it and how much it costs before any discounts or GST.
"""

import json
import os


def load_menu(data_path=None):
    """
    Load menu_data.json into a dictionary of {item_name: price}.
    You don't need to change this function.
    """
    if data_path is None:
        data_path = os.path.join(os.path.dirname(__file__), "menu_data.json")
    with open(data_path) as f:
        return json.load(f)


class Cart:
    """Holds one customer's cart: item names mapped to quantities."""

    def __init__(self, menu):
        """
        Store the given menu (a dict of {item_name: price}) so this cart
        can check prices, and set up an empty dictionary (self.items) to
        hold {item_name: quantity}.
        """
        self.menu = menu
        self.items = {}

    def add_item(self, item_name, quantity=1):
        """
        Add `quantity` of item_name to the cart.
        - If the item isn't on the menu, print
          "Sorry, {item_name} is not on the menu." and don't add it.
        - If the item is already in the cart, increase its quantity.
        - Otherwise, add it as a new entry.
        """
        if item_name not in self.menu:
            print(f'Sorry, {item_name} is not on the menu.')
            pass
        if item_name not in self.items:
            self.items[item_name] = quantity
        else:
            self.items[item_name] += quantity
        return self.items[item_name]

    def remove_item(self, item_name, quantity=1):
        """
        Remove `quantity` of item_name from the cart.
        - If removing would take the quantity to 0 or below, remove the
          item entirely.
        - If the item isn't in the cart, print "{item_name} isn't in the cart."
        """
        if item_name not in self.items:
            print(f"{item_name} isn't in the cart.")
            pass
        self.items[item_name] -= quantity
        if self.items[item_name] <= 0:
            del self.items[item_name]
        pass


    def get_subtotal(self):
        """
        Return the total price of everything in the cart BEFORE any
        discounts or tax, taking quantities into account
        (price * quantity for each item).
        """
        total = 0
        for item in self.items:
            total += self.menu[item] * self.items[item]
        return total


if __name__ == "__main__":
    menu = load_menu()
    cart = Cart(menu)
    cart.add_item("Coffee", 2)
    cart.add_item("Muffin", 1)
    print("Cart items:", cart.items)
    print("Subtotal:", cart.get_subtotal())
