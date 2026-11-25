MENU = {
    1: ("Burger", 50.0),
    2: ("Fries", 20.0),
    3: ("Soft Drink", 25.0),
}


def display_menu():
    print("\n===== MENU =====")
    for number, (name, price) in MENU.items():
        print(f"{number}. {name:<10} {price:.2f}")


def take_orders():
    orders = []

    while True:
        display_menu()

        try:
            choice = int(input("Enter item number (0 to finish): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 0:
            break

        if choice not in MENU:
            print("Invalid menu item.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a valid quantity.")
            continue

        if quantity <= 0:
            print("Quantity must be at least 1.")
            continue

        name, price = MENU[choice]
        orders.append({"item": name, "quantity": quantity, "price": price})
        print(f"Added {quantity} x {name}")

    return orders


def calculate_total(orders):
    return sum(order["quantity"] * order["price"] for order in orders)


def display_receipt(orders):
    print("\n========== RECEIPT ==========")

    if not orders:
        print("No items ordered.")
        print("=============================\n")
        return

    print(f"{'Item':<12}{'Qty':>5}{'Price':>12}{'Amount':>12}")
    print("-" * 41)

    for order in orders:
        amount = order["quantity"] * order["price"]
        print(
            f"{order['item']:<12}"
            f"{order['quantity']:>5}"
            f"{order['price']:>10.2f}"
            f"{amount:>10.2f}"
        )

    total = calculate_total(orders)
    print("-" * 41)
    print(f"{'TOTAL':<29}{total:>10.2f}")


def main():
    print("Welcome to the Ordering System")
    orders = take_orders()
    display_receipt(orders)


if __name__ == "__main__":
    main()

