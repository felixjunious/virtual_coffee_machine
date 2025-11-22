from coffee_machine import CoffeeMachine
from money_machine import MoneyMachine
from menu import Menu

def main():
    # Initialize Machines
    coffee_machine = CoffeeMachine()
    money_machine = MoneyMachine()

    # Preload Menu items:
    Menu.add_item("Espresso", 1.50, water=50, milk=0, coffee=18)
    Menu.add_item("Latte", 2.50, water=200, milk=150, coffee=24)
    Menu.add_item("Cappuccino", 3.00, water=250, milk=50, coffee=24)

    # Initial Resources
    coffee_machine.refill(water=1000, milk=1000, coffee=1000)

    # simple CLI program

    while True:
        print("\n--- Virtual Coffee Machine ---")
        Menu.show_items(with_ingredients=False)
        print("Type the 'drink name' to order a drink")
        print("Type 'report' to view machine resources.")
        print("Type 'quit' to exit.")

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

        drink = Menu.find_drink(choice)

        if not drink:
            print("Unknown selection. Please choose a valid drink.")
            continue

        # Check coffee machine's resources
        if not coffee_machine.has_sufficient_resources(drink):
            continue

        # Process payment
        if money_machine.handle_payment(drink.cost):
            coffee_machine.make_coffee(drink)

if __name__ == "__main__":
    main()