# Products Menu

products = {
    1: ("Burger", 50.0),
    2: ("Fries", 20.0),
    3: ("Soft Drink", 25.0),
}

selected_products = {}
total_cost = 0.0

while True:
    print("\nWelcome to the Products Menu")
    print("1. Burger - ₱50.0")
    print("2. Fries - ₱20.0")
    print("3. Soft Drink - ₱25.0")
    print("4. Finish selecting and order")

    try:
        product_choice = int(input("Please select a product (1-4): "))
    except ValueError:
        print("Invalid selection. Please enter a number from 1 to 4.")
        continue
    
    if product_choice == 4:
        break

    if product_choice not in products:
        print("Invalid selection. Please choose a valid product number (1-4).")
        continue

    if product_choice in selected_products:
        print("You already selected that product. Please choose a different one.")
        continue

    product_name, price = products[product_choice]

    try:
        quantity = int(input(f"Enter quantity for {product_name}: "))
    except ValueError:
        print("Invalid quantity. Please enter a whole number of 1 or more.")
        continue

    if quantity <= 0:
        print("Invalid quantity. Please enter 1 or more.")
        continue

    selected_products[product_choice] = (product_name, quantity, price)
    print(f"Added {quantity} {product_name}(s) to your order.")

print("\nYour order:")
if not selected_products:
    print("No products selected.")
else:
    for product_name, quantity, price in selected_products.values():
        item_cost = price * quantity
        total_cost += item_cost
        print(f"- {quantity} {product_name}(s) - ₱{item_cost:.2f}")

    print(f"Total cost: ₱{total_cost:.2f}")