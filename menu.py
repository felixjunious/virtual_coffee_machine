from menu_item import MenuItem

class Menu:
    """
    Manages all drink items available in the coffee machine menu.

    This class store MenuItem objects and provides helper methods
    for adding, removing, searching, and displaying menu items.
    """
    menu = []

    @classmethod
    def add_item(cls, name, cost, water, milk, coffee):
        """
        Add a new drink to the menu.

        Args:
            name (str): Name of the drink.
            cost (float): Price of the drink in euros.
            water (int): Amount of water required (ml).
            milk (int): Amount of milk required (ml).
            coffee (int): Amount of coffee required (g).

        Notes:
            If a drink with the same name already exists, it will not be added.
        """
        if cls.find_drink(name):
            print(f"Cannot add '{name}': a drink with this name already exists.")
            return

        ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

        cls.menu.append(MenuItem(name, cost, ingredients))
        print(f"Added '{name}' to the menu.")

    @classmethod
    def remove_item(cls, drink_name):
        """
        Remove a drink from the menu.

        Args:
            drink_name (str): Name of the drink to remove.
        """
        drink = cls.find_drink(drink_name)
        if not drink:
            print(f"Cannot remove '{drink_name}': drink not found")
            return
        cls.menu.remove(drink)
        print(f"Removed '{drink_name}' from the menu.")

    @classmethod
    def find_drink(cls, drink_name):
        """
        Look up a drink by name (case-insensitive).

        Args:
            drink_name (str): Name of the drink.

        Returns:
            MenuItem or None: The matched drink, if found.
        """
        for item in cls.menu:
            if item.name.lower() == drink_name.strip().lower():
                return item
        return None

    @classmethod
    def show_items(cls, with_ingredients=True):
        """
        Display the menu items.

        Args:
            with_ingredients (bool):
            If True, show ingredients for each drink.
            If False, display only names and prices.
        """
        if not cls.menu:
            print("Menu is empty.")
            return

        if with_ingredients:
            print(f"{'Name':<15} {'Price':<8} Ingredients")
            print("-" * 50)
            for item in cls.menu:
                ingredients_str = ", ".join(f"{k}: {v}" for k, v in item.ingredients.items())
                print(f"{item.name:<15} €{item.cost:<7.2f} {ingredients_str}")
        else:
            print(f"{'Name':<15} {'Price':<8}")
            print("-" * 25)
            for item in cls.menu:
                print(f"{item.name:<15} €{item.cost:<7.2f}")
