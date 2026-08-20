"""
CHALLENGE PART 3 of 4: The Receipt

See menu.py for an overview of this whole project. Complete menu.py and
order.py first, since this file needs both.

YOUR TASK (this file)
----------------------
Write a function that turns a finished Order into a nicely formatted
receipt string, including 10% GST (Australia's goods and services tax)
added on top of the subtotal.

EXAMPLE OUTPUT (for an order of 2 Coffee + 1 Muffin)
-----------------------------------------------------
--------- The Trendiest RECEIPT ---------
Coffee            x2      $9.00
Muffin            x1      $5.00
----------------------------------------
Subtotal:                $14.00
GST (10%):                $1.40
TOTAL:                   $15.40
----------------------------------------
"""

from order import Order

GST_RATE = 0.10


def generate_receipt(order: Order):
   """
    Build and return a multi-line string receipt for `order`, in the style
    shown in the EXAMPLE OUTPUT above.

    Steps:
      1. Start with a header line.
      2. For each item in order.items, add a line showing name, quantity,
         and that item's line total (price * quantity). You'll need the
         menu prices — order.menu.get_price(item_name) will give you them.
      3. Calculate the subtotal (order.get_subtotal()).
      4. Calculate GST as subtotal * GST_RATE.
      5. Calculate the final total as subtotal + GST.
      6. Add subtotal, GST, and total lines, each rounded to 2 decimal
         places (use round(value, 2)).
      7. Return the whole thing as one string (join lines with "\\n").
   """
   # 'gap' exists to space the text properly to align with the other text
   receipt = "-------------------------------\n"
   receipt += "---- The Trendiest RECEIPT ----\n"
   for item_name in order.items:
      quantity = order.items[item_name]
      item_total = quantity * order.menu.items[item_name]
      
      gap1 = 18 - len(item_name)
      gap2 = 10 - len(f"{item_total:.2f}")

      receipt += f"{item_name}{' '*gap1}x{quantity}{' '*gap2}${item_total:.2f}\n"

   receipt += "-------------------------------\n"

   subtotal = order.get_subtotal()
   gap = 21 - len(f"{subtotal:.2f}")
   receipt += f"Subtotal:{' '*gap}${subtotal:.2f}\n"

   gst = subtotal / 10
   gap = 20 - len(f"{gst:.2f}")
   receipt += f"GST (10%):{' '*gap}${gst:.2f}\n"

   total = subtotal + gst
   gap = 24 - len(f"{total:.2f}")
   receipt += f"TOTAL:{' '*gap}${total:.2f}\n"

   receipt += "-------------------------------\n"
   del gap, gap1, gap2
   return receipt
   



if __name__ == "__main__":
    from menu import Menu

    menu = Menu()
    order = Order(menu)
    order.add_item("Coffee", 2)
    order.add_item("Muffin", 1)
    print(generate_receipt(order))
