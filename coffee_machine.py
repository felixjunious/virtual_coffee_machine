class CoffeeMachine:
    """
    Represents the machine responsible for managing resources and preparing drinks.

    This class stores the available ingredients (water, milk, and coffee)
    and provides methods for reporting resources, checking availability,
    making drinks, and refilling the machine.
    """

    def __init__(self):
        """
        Initialize the coffee machine with empty ingredient resources.
        """
        self.resources = {
            "water": 0,
            "milk": 0,
            "coffee": 0,
        }

    def report(self):
        """
        Print the current amount of each resource in a formatted report.
        """
        print(f"{'Resource':<10} | Amount")
        print("-" * 22)
        print(f"{'Water':<10} | {self.resources['water']} ml")
        print(f"{'Milk':<10} | {self.resources['milk']} ml")
        print(f"{'Coffee':<10} | {self.resources['coffee']} g")

    def has_sufficient_resources(self, drink):
        """
        Check whether the machine has enough ingredients to make a given drink.

        Args:
            drink (MenuItem): The drink to check resources for.

        Returns:
            bool: True if all ingredients are sufficient, False otherwise.
        """
        for item, amount_required in drink.ingredients.items():
            if amount_required > self.resources.get(item, 0):
                print(f"Not enough {item} to make {drink.name}.")
                return False
        return True

    def make_coffee(self, drink):
        """
        Attempt to prepare the specified drink.

        Args:
            drink (MenuItem): The drink to prepare.

        Notes:
            If resources are insufficient, the drink will not be made.
        """
        if not self.has_sufficient_resources(drink):
            print(f"Can't make {drink.name}.")
            return

        for item, amount_required in drink.ingredients.items():
            self.resources[item] -= amount_required

        print(f"Here is your {drink.name} ☕️. Enjoy!")

    def refill(self, water=0, milk=0, coffee=0):
        """
        Add specified amounts of ingredients to the machine's resources.

        Args:
            water (int, optional): Amount of water to add in ml.
            milk (int, optional): Amount of milk to add in ml.
            coffee (int, optional): Amount of coffee to add in grams.
        """
        self.resources["water"] += water
        self.resources["milk"] += milk
        self.resources["coffee"] += coffee
