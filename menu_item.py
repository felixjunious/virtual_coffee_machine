from dataclasses import dataclass

@dataclass
class MenuItem:
    """
       Represents a drink that can be ordered from the coffee machine.

       Attributes:
           name (str): The name of the drink (e.g., "Latte").
           cost (float): Price of the drink in euros.
           ingredients (dict): A mapping of ingredient names to the quantities required.
                               Example: {"water": 200, "milk": 150, "coffee": 24}
       """
    name: str
    cost: float
    ingredients: dict

    def __str__(self):
        ingredients_str = ", ".join(f"{k}: {v}" for k, v in self.ingredients.items())
        return f"{self.name} - ${self.cost} ({ingredients_str})"


