from menu_item import MenuItem

class Menu:
    menu = []

    @classmethod
    def add_item(cls, name, cost, ingredients):
        if cls.find_drink(name):
            print(f"Cannot add '{name}': a drink with this name already exists.")
            return

        cls.menu.append(MenuItem(name, cost, ingredients))
        print(f"Added '{name}' to the menu.")

    @classmethod
    def remove_item(cls, drink_name):
        drink = cls.find_drink(drink_name)
        if not drink:
            print(f"Cannot remove '{drink_name}': drink not found")
            return
        cls.menu.remove(drink)
        print(f"Removed '{drink_name}' from the menu.")

    @classmethod
    def find_drink(cls, drink_name):
        for item in cls.menu:
            if item.name.lower() == drink_name.strip().lower():
                return item

        return None

    @classmethod
    def show_items(cls, with_ingredients=True):
        if not cls.menu:
            print("Menu is empty.")
            return

        if with_ingredients:
            print(f"{'Name':<15} {'Price':<8} Ingredients")
            print("-" * 50)
            for item in cls.menu:
                ingredients_str = ", ".join(f"{k}: {v}" for k, v in item.ingredients.items())
                print(f"{item.name:<15} ${item.cost:<7.2f} {ingredients_str}")
        else:
            print(f"{'Name':<15} {'Price':<8}")
            print("-" * 25)
            for item in cls.menu:
                print(f"{item.name:<15} ${item.cost:<7.2f}")



