#!/usr/bin/env python3
"""duck-typed annotations add"""
from typing import Union
from typing import Any
from typing import Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns first element of a list if exists, otherwise None"""
    if lst:
        return lst[0]
    return None
