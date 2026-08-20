"""
CHALLENGE PART 4 of 4: Putting It All Together

Complete menu.py, order.py, and receipt.py first. This file ties them all
together into a program you can actually run and use like a real POS.

YOUR TASK
---------
Write a loop that:
  1. Creates a Menu and an Order.
  2. Repeatedly asks the barista what item (and how many) to add, until
     they type "done".
  3. Once done, prints the final receipt using generate_receipt().

Run it with:
    python main.py
"""

from menu import Menu
from order import Order
from receipt import generate_receipt


def main():
    menu = Menu()
    order = Order(menu)

    print("The Trendiest POS — type an item name to add it, or 'done' to finish.")
    print("Available items:", ", ".join(menu.list_items()))

    # TODO: write a loop that:
    #   - asks for an item name
    #   - if it's "done", break out of the loop
    #   - otherwise ask for a quantity (convert the input to an int!)
    #   - call  `(item_name, quantity)

    print(generate_receipt(order))


if __name__ == "__main__":
    main()
