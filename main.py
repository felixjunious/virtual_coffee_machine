from coffee_machine import CoffeeMachine
from money_machine import MoneyMachine
from menu import Menu
from admin import admin_menu, authenticate

def main():
    # Initialize machines
    coffee_machine = CoffeeMachine()
    money_machine = MoneyMachine()

    # Initial drinks
    Menu.add_item("Espresso", 1.50, water=50, milk=0, coffee=18)
    Menu.add_item("Latte", 2.50, water=200, milk=150, coffee=24)
    Menu.add_item("Cappuccino", 3.00, water=250, milk=50, coffee=24)

    # Initial resources
    coffee_machine.refill(water=1000, milk=1000, coffee=1000)

    # Loop for CLI
    while True:
        print("\n--- Virtual Coffee Machine ---")
        Menu.show_items(with_ingredients=False)
        print("\nOptions:")
        print("Type the drink name to order a drink")
        print("Type 'report' to view machine resources and money info")
        print("Type 'menu' to view full menu with ingredients")
        print("Type 'admin' to enter admin mode")
        print("Type 'quit' to exit")

        choice = input("\nWhat would you like? ").strip().lower()

        if choice == "quit":
            print("Thanks for coming. Goodbye!")
            break

        elif choice == "report":
            coffee_machine.report()
            money_machine.report()
            continue

        elif choice == "menu":
            Menu.show_items(with_ingredients=True)
            continue

        elif choice == "admin":
            if authenticate():
                admin_menu(coffee_machine, money_machine)
            else:
                print("Incorrect password.")
            continue

        drink = Menu.find_drink(choice)
        if not drink:
            print("Unknown selection. Please choose a valid drink.")
            continue

        if not coffee_machine.has_sufficient_resources(drink):
            continue

        if money_machine.handle_payment(drink):
            coffee_machine.make_coffee(drink)

if __name__ == "__main__":
    main()
