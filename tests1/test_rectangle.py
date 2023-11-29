import pytest

from src.rectangle import Rectangle


@pytest.mark.rectangle
@pytest.mark.parametrize(("side_a", "side_b", "area"),
                         [
                             (5, 6, 30),
                             (5.5, 6.5, 35.75)
                         ], ids=["integer", "float"])
def test_rectangle_pos(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.get_area() == area


@pytest.mark.rectangle
def test_rectangle_pos_2(params_rectangle):
    side_a, side_b, area = params_rectangle
    r = Rectangle(side_a, side_b)
    assert r.get_area() == area


@pytest.mark.rectangle
@pytest.mark.parametrize(("side_a", "side_b", "area"),
                         [
                             (-5, -6, 30),
                             (-5.5, -6.5, 35.75),
                             (0, 0, 0)
                         ])
def test_rectangle_neg(side_a, side_b, area):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)
