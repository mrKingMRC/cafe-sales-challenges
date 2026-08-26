"""
CHALLENGE PART 1 of 4: The Menu

This project (pos_system) is split across several files that work
together:
    menu_data.json   - the raw menu data (already provided, don't edit)
    menu.py          - (this file) loads and looks up menu items
    order.py         - represents one customer's order
    receipt.py       - turns an order into a printable receipt
    main.py          - runs the whole program
    test_pos_system.py - automated checks for your code

Work through them in that order. Run `pytest` at any point to see which
parts are passing.

YOUR TASK (this file)
----------------------
Complete the Menu class so it loads menu_data.json and can answer
questions about what's available and how much things cost.
"""

import json
import os
from pathlib import Path


class Menu:
    """Loads and provides access to the café's menu."""

    def __init__(self, data_path="/workspaces/cafe-sales-challenges/01-cafe-pos/tier4_challenging/pos_system/menu_data.json"):
        with open(data_path) as f:
            self.items = json.load(f)

    def has_item(self, item_name):
        if item_name in self.items: 
            return True
        else: 
            return False

    def get_price(self, item_name):
        if self.has_item(item_name):
            item_price = self.items[item_name]
            return item_price
        else:
            return 0
        


    def list_items(self):
        self.__init__


if __name__ == "__main__":
    # Quick manual check while you're building this file.
    # (main.py will use this class properly later.)
    menu = Menu()
    print("Menu items:", menu.list_items())
    print("Price of Coffee:", menu.get_price("Coffee"))
    print("Has Pizza?", menu.has_item("Pizza"))
