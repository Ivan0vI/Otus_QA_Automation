import pytest


@pytest.fixture(scope="session")
def params_circle():
    yield 1


@pytest.fixture(scope="session")
def params_rectangle():
    yield 5, 6, 30


@pytest.fixture(scope="session")
def params_square():
    yield 5, 10


@pytest.fixture(scope="session")
def params_triangle():
    yield 5, 5, 5, 5, 12.5
