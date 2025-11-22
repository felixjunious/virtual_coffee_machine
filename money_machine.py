class MoneyMachine:
    # Coin values in EUR
    COINS = {
        "2€": 2.00,
        "1€": 1.00,
        "50c": 0.50,
        "20c": 0.20,
        "10c": 0.10,
        "5c": 0.05,
        "2c": 0.02,
        "1c": 0.01,
    }

    def __init__(self):
        # Tracks total revenue collected
        self.revenue = 0.0

    def report(self):
        """Display how much money the machine has collected."""
        print(f"Revenue collected: €{self.revenue:.2f}")

    def _collect_coins(self):
        """
        Ask the user how many coins they want to insert of each type.
        Returns the total amount inserted in euros.
        """
        print("\n--- Coin Insertion ---")
        print("Enter how many coins you are inserting for each type.")
        print("If none, type 0.\n")

        inserted_total = 0.0

        for coin_type, coin_value in self.COINS.items():
            while True:
                try:
                    count = int(input(f"How many '{coin_type}' coins? "))
                    if count < 0:
                        print("Please enter a non-negative number.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            inserted_total += count * coin_value

        print(f"\nTotal inserted: €{inserted_total:.2f}\n")
        return round(inserted_total, 2)

    def handle_payment(self, cost):
        """
        Handle payment for a drink.
        Returns True if payment is accepted, False otherwise.
        """
        paid_amount = self._collect_coins()

        if paid_amount < cost:
            print("Not enough money. Refunding...")
            return False

        if paid_amount > cost:
            change = round(paid_amount - cost, 2)
            print(f"Change returned: €{change:.2f}")

        self.revenue += cost
        return True
