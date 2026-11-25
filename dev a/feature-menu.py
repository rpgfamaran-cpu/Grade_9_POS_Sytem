# Developer A: product selection

PRODUCTS = {
    1: ("Burger", 50.0),
    2: ("Fries", 20.0),
    3: ("Soft Drink", 25.0),
}


def display_menu():
    print("\n===== PRODUCTS MENU =====")
    for number, (name, price) in PRODUCTS.items():
        print(f"{number}. {name:<12} ₱{price:.2f}")
    print("4. Finish selecting and order")


def take_orders():
    selected_orders = []
    selected_numbers = set()

    while True:
        display_menu()

        try:
            choice = int(input("Please select a product (1-4): "))
        except ValueError:
            print("Invalid selection. Please enter a number from 1 to 4.")
            continue

        if choice == 4:
            break

        if choice not in PRODUCTS:
            print("Invalid selection. Please choose a valid product number (1-4).")
            continue

        if choice in selected_numbers:
            print("You already selected that product. Please choose a different one.")
            continue

        name, price = PRODUCTS[choice]

        try:
            quantity = int(input(f"Enter quantity for {name}: "))
        except ValueError:
            print("Invalid quantity. Please enter a whole number of 1 or more.")
            continue

        if quantity <= 0:
            print("Invalid quantity. Please enter 1 or more.")
            continue

        selected_numbers.add(choice)
        selected_orders.append({"item": name, "quantity": quantity, "price": price})
        print(f"Added {quantity} x {name}")

    return selected_orders


if __name__ == "__main__":
    take_orders()