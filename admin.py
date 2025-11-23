from menu import Menu

ADMIN_PASSWORD = "admin123"

def admin_menu(coffee_machine, money_machine):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Refill resources")
        print("2. Add drink")
        print("3. Remove drink")
        print("4. View reports")
        print("5. Reset revenue/profit")
        print("6. Exit admin menu")

        choice = int(input("select an option: ").strip())

        if choice == 1:
            water = int(input("Add water (ml): "))
            milk = int(input("Add milk (ml): "))
            coffee = int(input("Add coffee (g): "))
            coffee_machine.refill(water, milk, coffee)
            print("Resources refilled.")

        elif choice == 2:
            name = input("Drink name: ")
            cost = float(input("Drink cost (€): "))
            water = int(input("Water needed (ml): "))
            milk = int(input("Milk needed (ml): "))
            coffee = int(input("Coffee needed (g): "))
            Menu.add_item(name, cost, water, milk, coffee)

        elif choice == 3:
            name = input("Drink name to remove: ")
            Menu.remove_item(name)

        elif choice == 4:
            coffee_machine.report()
            money_machine.report()

        elif choice == 5:
            confirm = input("Reset revenue and profit? (yes/no): ").strip().lower()
            if confirm == "yes":
                money_machine.revenue = 0.0
                money_machine.profit = 0.0
                print("Revenue and profit reset.")

        elif choice == 6:
            print("Exiting admin menu.")
            break
        else:
            print("Invalid choice. Try again.")

def authenticate():
    password = input("Enter admin password: ")
    return password == ADMIN_PASSWORD