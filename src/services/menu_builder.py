from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def get_ingredients(self, recipe) -> List[str]:
        ingredients = [ingredient.name for ingredient in recipe.keys()]
        return ingredients

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        menu = []
        for dish in self.menu_data.dishes:
            if restriction in dish.get_restrictions():
                continue
            menu_item = {
                "dish_name": dish.name,
                "ingredients": self.get_ingredients(dish.recipe),
                "price": dish.price,
                "restrictions": dish.get_restrictions(),
            }

            menu.append(menu_item)

        return menu
