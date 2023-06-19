from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    carne = Ingredient("carne")
    carne2 = Ingredient("carne")
    bacon = Ingredient("bacon")

    assert carne.__hash__() == carne2.__hash__()
    assert carne.__hash__() != bacon.__hash__()
    assert carne.__repr__() == "Ingredient('carne')"
    assert carne.__eq__(carne2) is True
    assert carne.__eq__(bacon) is False
    assert carne.name == "carne"
    assert carne.restrictions == {Restriction.ANIMAL_DERIVED,
                                  Restriction.ANIMAL_MEAT}
