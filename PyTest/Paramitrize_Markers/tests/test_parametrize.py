import pytest

from PyTest.Paramitrize_Markers.App.app import add


def test_validate_add_num():
    assert add(5, 10) == 15


def test_validate_add_str():
    assert add('Hello ', 'Pytest') == "Hello Pytest"


def test_validate_add_list():
    assert add([1, 2], [3]) == [1, 2, 3]


# parametrize: we can create own parameters and pass to pytest function
@pytest.mark.parametrize("a,b,c", [(1, 2, 3), ('Hello ', 'Pytest', "Hello Pytest"), ([1, 2], [3], [1, 2, 3])])
def test_valid_add(a, b, c):
    assert add(a, b) == c


# parametrize: we can create own parameters and pass to pytest function
@pytest.mark.parametrize("a,b,c", [(1, 2, 3), ('Hello ', 'Pytest', "Hello Pytest"), ([1, 2], [3], [1, 2, 3])], ids=['with int', 'with str', 'with list'])
def test_valid_add(a, b, c):
    assert add(a, b) == c

