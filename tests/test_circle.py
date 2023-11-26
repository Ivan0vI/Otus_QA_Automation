import pytest

from src.circle import Circle


@pytest.mark.circle
@pytest.mark.parametrize(("r", "pi", "area"),
                         [
                             (1, 3.14159, 3.14159),
                             (1.5, 3.14159, 7.068577499999999)
                         ], ids=["float", "float"])
def test_circle_pos(r, pi, area):
    print("\nТест проверяет построение круга")
    c = Circle(r, "Circle")
    assert c.get_area() == area


@pytest.mark.circle
def test_circle_pos_2(params_circle):
    print("\nТест проверяет построение круга")
    r = params_circle
    c = Circle(r, "Circle")
    assert c.get_area() == 3.14159


@pytest.mark.circle
@pytest.mark.parametrize(("r", "pi", "area"),
                         [
                             (-1, 3.14159, 3.14159),
                             (-1.5, 3.14159, 7.068577499999999),
                             (0, 3.14159, 0)
                         ], ids=["float", "float", "integer"])
def test_circle_neg(r, pi, area):
    with pytest.raises(ValueError):
        Circle(r, "Circle")
