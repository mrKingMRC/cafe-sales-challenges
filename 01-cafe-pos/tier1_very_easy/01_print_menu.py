"""
CHALLENGE: Print the Café Menu
DIFFICULTY: Very, very easy
FOLDER: 01-cafe-pos / tier1_very_easy

STORY
-----
It's opening day at The Trendiest Café! The chalkboard menu fell off the wall
and smashed. Before customers arrive, you need to recreate it on the
computer screen using Python's print() function.

YOUR TASK
---------
The menu information is already stored in the variables below. Using
print(), display the menu EXACTLY like the example output shown below.
Find every line marked "# TODO" and write ONE print() statement there.

Hint: You can join text and numbers together in a single print() using
an f-string, like this:
    print(f"1. {item_1_name} - ${item_1_price}")

EXAMPLE OUTPUT
--------------
==============================
The Trendiest CAFE - TODAY'S MENU
==============================
1. Coffee - $4.5
2. Tea - $3.5
3. Muffin - $5.0
4. Toastie - $6.5
==============================
"""

item_1_name = "Coffee"
item_1_price = 4.50
item_2_name = "Tea"
item_2_price = 3.50
item_3_name = "Muffin"
item_3_price = 5.00
item_4_name = "Toastie"
item_4_price = 6.50

# DONE 1: print a line of exactly 30 equals signs: "=============================="
print("==============================")
# DONE 2: print the title line: "The Trendiest CAFE - TODAY'S MENU"
print("The Trendiest CAFE - TODAY'S MENU")
# DONE 3: print another line of 30 equals signs
print("==============================")
# DONE 4: print item 1 using item_1_name and item_1_price (see example output)
print(f"1. {item_1_name} - ${item_1_price}")
# TODO 5: print item 2 using item_2_name and item_2_price
# TODO 6: print item 3 using item_3_name and item_3_price
# TODO 7: print item 4 using item_4_name and item_4_price
# TODO 8: print a final line of 30 equals signs


# ---------------------------------------------------------------
# Don't change anything below this line.
# This just reminds you what to check once you've finished.
# ---------------------------------------------------------------
print("\n(Check: does your output above match the EXAMPLE OUTPUT exactly?)")
