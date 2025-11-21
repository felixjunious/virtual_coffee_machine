from dataclasses import dataclass

@dataclass
class MenuItem:
    name: str
    cost: float
    ingredients: dict

    def __str__(self):
        ingredients_str = ", ".join(f"{k}: {v}" for k, v in self.ingredients.items())
        return f"{self.name} - ${self.cost} ({ingredients_str})"


