class MoneyMachine:
    # Coin values in EUR
    COINS = {
        "2E": 2.00,
        "1E": 1.00,
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
        """Ask the user for coin counts and return the total inserted amount."""
        print("Insert coins (Euro):")
        inserted_total = 0.0

        for coin_type, coin_value in self.COINS.items():
            try:
                amount = int(input(f"{coin_type}: "))
            except ValueError:
                print("Invalid number. Using 0.")
                amount = 0
            inserted_total += amount * coin_value

        return round(inserted_total, 2)

    def process_payment(self, cost):
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
