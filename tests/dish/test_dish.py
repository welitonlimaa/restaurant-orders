from src.models.dish import Dish  # noqa: F401, E261, E501
from models.ingredient import Ingredient
from models.ingredient import Restriction
import pytest


# Req 2
def test_dish():
    lasanha = Dish("Lasanha", 25.0)
    pizza = Dish("Pizza", 30.0)
    assert repr(lasanha) == "Dish('Lasanha', R$25.00)"
    assert repr(pizza) == "Dish('Pizza', R$30.00)"

    assert lasanha == Dish("Lasanha", 25.0)
    assert pizza == Dish("Pizza", 30.0)

    assert lasanha.__hash__() == Dish("Lasanha", 25.0).__hash__()
    assert lasanha.__hash__() != pizza.__hash__()

    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("frango")
    lasanha.add_ingredient_dependency(ingredient1, 2)
    lasanha.add_ingredient_dependency(ingredient2, 1)
    assert lasanha.recipe == {ingredient1: 2, ingredient2: 1}

    ingredient3 = Ingredient("bacon")
    ingredient4 = Ingredient("queijo mussarela")
    pizza.add_ingredient_dependency(ingredient3, 3)
    pizza.add_ingredient_dependency(ingredient4, 1)
    assert pizza.name == "Pizza"
    assert pizza.get_restrictions() == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED}

    assert lasanha.get_ingredients() == {ingredient1, ingredient2}
    assert pizza.get_ingredients() == {ingredient3, ingredient4}

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Spaghetti", "25.0")

    with pytest.raises(ValueError,
                       match="Dish price must be greater then zero."):
        Dish("Spaghetti", 0.0)
