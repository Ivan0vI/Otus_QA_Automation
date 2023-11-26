import pytest

from src.triangle import Triangle


@pytest.mark.triangle
@pytest.mark.parametrize(("side_a", "side_b", "base", "height", "area"),
                         [
                             (5, 5, 5, 5, 12.5),
                             (5.5, 5.5, 5.5, 5.5, 15.125)
                         ], ids=["integer", "float"])
def test_triangle_pos(side_a, side_b, base, height, area):
    print("\nТест проверяет построение треугольника")
    t = Triangle(side_a, side_b, base, height)
    assert t.get_area() == area


@pytest.mark.triangle
def test_triangle_pos_2(params_triangle):
    print("\nТест проверяет построение треугольника")
    side_a, side_b, base, height, area = params_triangle
    t = Triangle(side_a, side_b, base, height)
    assert t.get_area() == area


@pytest.mark.triangle
@pytest.mark.parametrize(("side_a", "side_b", "base", "height", "area"),
                         [
                             (-5, 5, 5, 5, 12.5),
                             (-5.5, 5.5, 5.5, 5.5, 15.125),
                             (0, 0, 0, 0, 0)
                         ], ids=["integer", "float", "integer"])
def test_triangle_neg(side_a, side_b, base, height, area):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, base, height)
