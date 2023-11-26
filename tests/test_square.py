import pytest

from src.square import Square


@pytest.mark.square
@pytest.mark.parametrize(("side_a", "area"),
                         [
                             (5, 10),
                             (5.5, 11.0)
                         ], ids=["integer", "float"])
def test_square_pos(side_a, area):
    print("\nТест проверяет построение квадрата")
    s = Square(side_a)
    assert s.get_area() == area


@pytest.mark.square
def test_square_pos_2(params_square):
    print("\nТест проверяет построение квадрата")
    side_a, area = params_square
    s = Square(side_a)
    assert s.get_area() == area


@pytest.mark.square
@pytest.mark.parametrize(("side_a", "area"),
                         [
                             (-5, 10),
                             (-5.5, 11.0),
                             (0, 0)
                         ], ids=["integer", "float", "integer"])
def test_rectangle_neg(side_a, area):
    with pytest.raises(ValueError):
        Square(side_a)
