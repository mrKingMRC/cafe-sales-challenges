MENU = {
    "Coffee": 4.50,
    "Tea": 3.50,
    "Muffin": 5.00,
    "Toastie": 6.50,
    "Hot Chocolate": 4.00,
}
order_item = input("What would you like? ")
if order_item in MENU:
   print(f"Good Choice! {order_item} will cost ${MENU[order_item]}!")
else:
   print(f"Sorry we do not currently have {order_item} in stock")
