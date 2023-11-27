import pytest


@pytest.fixture(scope="session")
def params_circle():
    print("\nВвод данных для построения круга")
    yield 1


@pytest.fixture(scope="session")
def params_rectangle():
    print("\nВвод данных для построения треугольника")
    yield 5, 6, 30


@pytest.fixture(scope="session")
def params_square():
    print("\nВвод данных для построения квадрата")
    yield 5, 10


@pytest.fixture(scope="session")
def params_triangle():
    print("\nВвод данных для построения треугольника")
    yield 5, 5, 5, 5, 12.5
