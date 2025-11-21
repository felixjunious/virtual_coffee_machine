class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 0,
            "milk": 0,
            "coffee": 0,
        }

    def report(self):
        print(f"{'Resource':<10} | Amount")
        print("-" * 22)
        print(f"{'Water':<10} | {self.resources['water']} ml")
        print(f"{'Milk':<10} | {self.resources['milk']} ml")
        print(f"{'Coffee':<10} | {self.resources['coffee']} g")

    def has_sufficient_resources(self, drink):
        for item, amount_required in drink.ingredients.items():
            if amount_required > self.resources.get(item, 0):
                print(f"Not enough {item} to make {drink.name}.")
                return False
        return True

    def make_coffee(self, drink):
        if not self.has_sufficient_resources(drink):
            print(f"Can't make {drink.name}.")
            return

        for item, amount_required in drink.ingredients.items():
            self.resources[item] -= amount_required

        print(f"Here is your {drink.name} ☕️. Enjoy!")

    def refill(self, water=0, milk=0, coffee=0):
        self.resources["water"] += water
        self.resources["milk"] += milk
        self.resources["coffee"] += coffee
