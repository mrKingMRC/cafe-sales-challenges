"""
CHALLENGE PART 2 of 4: The Checkout

See cart.py for an overview of this whole project. Complete cart.py first,
since this file needs it.

YOUR TASK (this file)
----------------------
Build a Checkout class that takes a finished Cart and works out the final
amount owed, applying (in this exact order):
    1. A loyalty discount, if the customer is a loyalty member (10% off
       the subtotal).
    2. A percentage-off voucher code, if one is supplied.
    3. 10% GST on top of whatever is left.
Then produce a nicely formatted receipt string.

VOUCHER CODES
-------------
    "SAVE10" -> 10% off
    "SAVE20" -> 20% off
    anything else / None -> no discount, print "Invalid voucher code."

EXAMPLE OUTPUT (Cart of 2 Coffee + 1 Muffin, loyalty member, voucher "SAVE10")
-------------------------------------------------------------------------------
--------- The Trendiest RECEIPT ---------
Coffee            x2      $9.00
Muffin            x1      $5.00
----------------------------------------
Subtotal:                $14.00
Loyalty discount (10%):   -$1.40
Voucher SAVE10 (10%):     -$1.26
GST (10%):                $1.13
TOTAL:                   $12.47
----------------------------------------
"""

GST_RATE = 0.10
LOYALTY_DISCOUNT_RATE = 0.10

VOUCHER_CODES = {
    "SAVE10": 0.10,
    "SAVE20": 0.20,
}


class Checkout(object):
    """Turns a finished Cart into a final total and a printable receipt."""

    def __init__(self, cart, is_loyalty_member=False, voucher_code=None):
        """
        Store the cart, whether the customer is a loyalty member, and an
        optional voucher_code string (or None).
        """
        self.cart = cart
        self.is_loyalty_member = is_loyalty_member
        self.voucher_code = voucher_code

    def calculate_total(self):
        """
        Work out and return the final total owed, applying discounts and
        GST IN THIS EXACT ORDER:
          1. Start with self.cart.get_subtotal().
          2. If self.is_loyalty_member, reduce the running total by
             LOYALTY_DISCOUNT_RATE (10%).
          3. If self.voucher_code is a valid key in VOUCHER_CODES, reduce
             the running total by that percentage. If it's set but NOT a
             valid key, print "Invalid voucher code." and apply no
             voucher discount.
          4. Add GST (GST_RATE) on top of whatever remains.
        Return the final total, rounded to 2 decimal places.
        """
        subtotal = self.cart.get_subtotal()
        if self.is_loyalty_member:
            subtotal *= 0.9
        
        ...

    def generate_receipt(self):
        """
        Build and return a multi-line string receipt, in the style shown
        in the EXAMPLE OUTPUT above. Only include a "Loyalty discount"
        line if self.is_loyalty_member, and only include a "Voucher"
        line if self.voucher_code is a valid code in VOUCHER_CODES.

        Steps:
          1. Header line: "--------- The Trendiest RECEIPT ---------"
          2. For each item in self.cart.items, a line with name, quantity
             and that item's line total (price * quantity). Use
             self.cart.menu[item_name] to look up the price.
          3. A divider line of 40 dashes.
          4. Subtotal line.
          5. Loyalty discount line (if applicable), shown as a negative
             dollar amount.
          6. Voucher line (if applicable), shown as a negative dollar
             amount.
          7. GST line.
          8. TOTAL line — call self.calculate_total() for this.
          9. A final divider line of 40 dashes.
          10. Join every line with "\\n" and return the whole string.
        """
        # TODO: implement this method
        pass


if __name__ == "__main__":
    from cart import Cart, load_menu

    menu = load_menu()
    cart = Cart(menu)
    cart.add_item("Coffee", 2)
    cart.add_item("Muffin", 1)

    checkout = Checkout(cart, is_loyalty_member=True, voucher_code="SAVE10")
    print(checkout.generate_receipt())
