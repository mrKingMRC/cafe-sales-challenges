MENU = {
    "Coffee": 4.50,
    "Tea": 3.50,
    "Muffin": 5.00,
    "Toastie": 6.50,
    "Hot Chocolate": 4.00,
}

ordertotal = 0

running = True
while running:
   order = input("What would you like? ")
   if order in MENU:
      ordertotal += MENU[order]
      print(f"{order} ${MENU[order]}")
      print(f"Your total is ${ordertotal}")
      print(f'Type "done" to finish your order.')
   elif order == "done":
      print("Thanks for ordering! Your item will be ready soon.")
      running = False
   else:
      print('Item or command not found. Please try again or type "done" to finish.')

