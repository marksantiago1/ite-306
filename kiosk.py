menu = {
    "Pizza": 8.99,
    "Milk Tea": 3.49,
    "Coffee": 2.99,
    "Burger": 5.99,
    "Soda": 1.49
}

print("Welcome to the Food and Drink Kiosk!")
print("MENU:")


for item, price in menu.items():
    print(f"{item}: ${price:.2f}")


user_choice = input("Enter the name you want to order: ")

if user_choice in menu:
    quantity = int(input("Enter the quantity: "))
    if quantity <= 0:
        print("Invalid quantity.")
    else:
        total_price = menu[user_choice] * quantity
        print("\nBILL:")
        print(f"Item: {user_choice}")
        print(f"Quantity: {quantity}")
        print(f"Total Price: ${total_price:.2f}")
        print("Thank you for using my Food and Drink Kiosk!")
else:
    print("Invalid choice.")
