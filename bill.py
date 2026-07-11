import time
menu = {
    "Coffee": {
        "Espresso": 110,
        "Americano": 130,
        "Cappuccino": 160,
        "Latte": 170,
        "Mocha": 190,
        "Cold Coffee": 180,
        "Caramel Frappé": 220
    },

    "Tea": {
        "Masala Tea": 70,
        "Green Tea": 90,
        "Lemon Tea": 80,
        "English Breakfast Tea": 120,
        "Iced Tea": 140
    },

    "Bakery & Pastries": {
        "Butter Croissant": 120,
        "Chocolate Croissant": 150,
        "Blueberry Muffin": 130,
        "Chocolate Muffin": 130,
        "Cinnamon Roll": 160,
        "Banana Bread": 140
    },

    "Sandwiches & Snacks": {
        "Veg Grilled Sandwich": 180,
        "Chicken Grilled Sandwich": 240,
        "Garlic Bread": 140,
        "French Fries": 120,
        "Cheese Fries": 170,
        "Nachos with Salsa": 190
    },

    "Cakes & Desserts": {
        "Chocolate Brownie": 170,
        "Cheesecake": 240,
        "Red Velvet Cake": 220,
        "Tiramisu": 260,
        "Chocolate Lava Cake": 230,
        "Vanilla Ice Cream": 120
    },

    "Cold Beverages": {
        "Fresh Lime Soda": 90,
        "Oreo Milkshake": 210,
        "Chocolate Milkshake": 220,
        "Strawberry Smoothie": 230,
        "Mango Smoothie": 230,
        "Bottled Water": 30
    }
}

print(" Welcome to Coffee & Crumbs Cafe")
print("=================================")
print("         - MENU -")
for category,item in menu.items():
    print(f"\n{category}")
    print("--------------------")
    for dish,price in item.items():
        print(f"     {dish}:{price}")
print("Please type 'done' once you have finished your order\n") 

order=[]
total=0
while True:
    choice=input("what would you like to order?\n").strip().title()
    if choice=="Done":
         break 
    for category, items in menu.items():
        if choice in items:
            print("Order is available")
            quantity_ = input("Please enter the quantity of the order: ")
            if quantity_.isdigit():
                quantity = int(quantity_)
                if quantity > 0:
                    item_cost = items[choice] * quantity
                    total += item_cost
                    order.append(f"{choice} × {quantity} = ₹{item_cost}")
                    break
                else:
                     print("Please enter a quantity greater than 0.")
            else:
                print("Please enter a valid quantity.")        
    else:
            print("Sorry order is not availabele in cart." \
            "Please recheck spelling of order")

print("\n====================================")
print("     OFFICIAL RECEIPT ")
print("====================================")
if len(order)==0:
     print("No order placed. Thank you for visiting Coffee & Crumbs Cafe!")
     exit()
else:
    for item in order:
           print(f"{item}")
           print("-------------------------------")
    print(f"Subtotal:{total}")
    print("-------------------------------")
tax=total*0.05
print(f"Tax(5%):{tax}")
if total>500:
     discount=total*0.10
     print(f"Discount(10%):{discount}")
     grand_total=total+tax-discount
     print(f"GRAND TOTAL:{grand_total}")
else:
     grand_total=total+tax
     print(f"GRAND TOTAL:{grand_total}")
print("====================================") 
print(" Payment Successful! Thank you. ")
print("====================================\n")  
print("Please wait while we prepare your order...")
time.sleep(5)
print("\n ORDER IS READY! Please collect it at the counter. Enjoy your meal! ")


     
