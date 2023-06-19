import csv
from typing import Dict, Set

from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes: Set[Dish] = set()
        self.ingredients: Dict[str, Ingredient] = {}

        self.get_data(source_path)

    def insert_dish(self, dish):
        self.dishes.add(dish)

    def get_dish(self, dish):
        for curr_dish in self.dishes:
            if curr_dish == dish:
                return curr_dish

    def insert_or_get_dish(self, name: str, price: float):
        dish = Dish(name, price)
        if dish not in self.dishes:
            self.insert_dish(dish)
        else:
            return self.get_dish(dish)
        return dish

    def insert_ingredient(self, name):
        ingredient = Ingredient(name)
        self.ingredients[name] = ingredient
        return ingredient

    def get_ingredient(self, name):
        return self.ingredients[name]

    def insert_or_get_ingredient(self, name: str):
        if name not in self.ingredients:
            return self.insert_ingredient(name)
        else:
            return self.get_ingredient(name)

    def get_data(self, source_path: str):
        with open(source_path, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                dish_name = row[0]
                dish_price = float(row[1])
                ingredient_name = row[2]
                ingredient_quantity = int(row[3])

                dish = self.insert_or_get_dish(dish_name, dish_price)
                ingredient = self.insert_or_get_ingredient(ingredient_name)

                dish.add_ingredient_dependency(ingredient, ingredient_quantity)
