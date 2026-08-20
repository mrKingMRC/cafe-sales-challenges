"""
CHALLENGE: Rebuild Ordering With Functions
DIFFICULTY: Intermediate
FOLDER: 01-cafe-pos / tier3_intermediate

STORY
-----
The head barista wants the ordering logic cleaned up so different parts of
the café's system can reuse it. Instead of one long block of code, you'll
break the logic into three separate functions.

YOUR TASK
---------
Implement the three functions below (read each docstring carefully), then
use them together in the `if __name__ == "__main__":` section at the
bottom to run a full ordering loop.

EXAMPLE OUTPUT
--------------
What would you like? (type 'done' to finish): Coffee
Added Coffee - $4.5
What would you like? (type 'done' to finish): Muffin
Added Muffin - $5.0
What would you like? (type 'done' to finish): done

----- RECEIPT -----
Coffee            $4.50
Muffin            $5.00
--------------------
TOTAL:            $9.50
"""

MENU = {
    "Coffee": 4.50,
    "Tea": 3.50,
    "Muffin": 5.00,
    "Toastie": 6.50,
    "Hot Chocolate": 4.00,
}


def get_price(item_name):
    """
    Return the price of item_name from MENU, or None if it isn't on the menu.

    Example:
        get_price("Tea") -> 3.5
        get_price("Pizza") -> None
    """
    # TODO: implement this function
    if item_name not in MENU:
        raise Exception("Item not on menu")
    return MENU[item_name]


def calculate_total(order_list):
    """
    order_list is a list of item names, e.g. ["Coffee", "Muffin"].
    Return the sum of all their prices (use get_price() to look each one up).
    Skip any item that isn't found on the menu (don't crash!).

    Example:
        calculate_total(["Coffee", "Muffin"]) -> 9.5
    """
    total = 0.0
    for item in order_list:
        Total += get_price(item)
    return total


def display_receipt(order_list, total):
    """
    Print a neatly formatted receipt for order_list, followed by the total,
    matching the style shown in the EXAMPLE OUTPUT above.
    """
    # TODO: implement this function
    print("----- RECEIPT -----")
    for item in order_list:
        print(f"{item}            ${get_price(item)}")
    print("--------------------")
    print(f"TOTAL:            $f{total}")


if __name__ == "__main__":
    order_list = []

    # TODO: write a while loop (like in tier2) that asks the customer what
    # they'd like, adds valid items to order_list, and stops when they type
    # 'done'
    while True:
        item = input("What would you like? (type 'done' to finish): ")
        try:
            price = get_price(item)
            print(f"Added {item} - ${price}")
            order_list.append(item)
        except Exception as e:
            print("not on menu")

    # TODO: once the loop is done, call calculate_total() and then
    # display_receipt() to show the final receipt.
    total = calculate_total(order_list)
    display_receipt(order_list, total)
