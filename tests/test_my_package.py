""" tests for my_package """

from .context import my_package


def test_increment():
    """ test increment """
    assert my_package.increment(3) == 4


def test_decrement():
    """ test decrement """
    assert my_package.decrement(3) == 2
