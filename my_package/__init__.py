""" my_package was created to learn how to create packages """

from .plotsyn import execute
from .inc_dec import increment, decrement, double

# optional list of names to be exported when import * is used
__all__ = ["execute", "increment", "decrement", "double"]
