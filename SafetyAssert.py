from enum import Enum
from typing import NoReturn

class Color(Enum):
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"

def exhaustiveness_check(value: NoReturn) -> NoReturn:
    assert False, 'This code should never be reached, got: {0}'.format(value)

# python -m pip install -U mypy

def some_func(color: Color) -> str:
    match color:
        case Color.RED:
            return "Color is red."
        case Color.GREEN:
            return "Color is green."
    exhaustiveness_check(color)

some_func(Color.RED)
# `mypy examples.py` leads to:
# ...error: Argument 1 to "exhaustiveness_check" has incompatible type "Literal[Color.BLUE]"; expected "NoReturn"
