class PizzaDelivery:
    def __init__(self, name, price, ingredients, ordered=False):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = ordered

    def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        self.price += quantity * ingredient_price
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += 1
        else:
            self.ingredients[ingredient] = quantity

    def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif self.ingredients[ingredient] < quantity:
            return f"Please check again the desired quantity of {ingredient}!"
        else:
            self.ingredients[ingredient] -= quantity
            self.price -= quantity * ingredient_price

    def make_order(self):
        if self.ordered:
            return f"Pizza {self.name} already prepared and we can't make any changes!"
        self.ordered = True
        ingr = f"{', '.join([f'{key}: {value}' for key, value in self.ingredients.items()])}"
        res = f"You\'ve ordered pizza {self.name} prepared with {ingr} and the price will be {self.price}lv."
        return res


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
