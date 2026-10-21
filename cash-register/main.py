
from cash_register import CashRegister

discount_input = input("Enter discount percentage (press Enter for 0): ")

if discount_input.strip() == "":
    discount = 0
else:
    try:
        discount = int(discount_input)
    except ValueError:
        discount = -1

register = CashRegister(discount)

while True:
    print("\n--- CASH REGISTER ---")
    print("1. Add item")
    print("2. Apply discount")
    print("3. Void last transaction")
    print("4. View items and total")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter item name: ")

        try:
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))
            register.add_item(item, price, quantity)
        except ValueError:
            print("Enter a valid price and quantity.")

    elif choice == "2":
        register.apply_discount()

    elif choice == "3":
        register.void_last_transaction()

    elif choice == "4":
        print("Items:", register.items)
        print(f"Total: {register.total:.2f}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
