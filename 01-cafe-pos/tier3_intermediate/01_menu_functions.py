MENU = {
    "Coffee": 4.50,
    "Tea": 3.50,
    "Muffin": 5.00,
    "Toastie": 6.50,
    "Hot Chocolate": 4.00,
}
def get_price(item_name):
    if item_name in MENU:
        return MENU[item_name]
    else: 
        return 0

def calculate_total(order_list):
    total = 0
    for item_name in order_list:
        total += get_price(item_name)

    return total

def display_receipt(order_list, total):
    print("----------RECEIPT----------")
    for item_name in order_list:
        print(f"{item_name}{' ' * (23-len(item_name))}${MENU[item_name]}")
    print("---------------------------")
    print(f"Your total is ${calculate_total(order_list)}")

if __name__ == "__main__":
    running = True
    order_list = []
    while running:
        item_name = input(".")
        order_list.append(item_name)
        price = get_price(item_name)
        if item_name in MENU:
            print(f"Added {item_name} to your order!")
            print(f"Your current total is ${calculate_total(order_list)}")
        elif item_name == "Finish":
            order_list = [item_name for item_name in order_list if item_name in MENU]
            total = calculate_total(order_list)
            display_receipt(order_list, total)
        else:
            print(f"We do not currently have {item_name} in stock")
        




