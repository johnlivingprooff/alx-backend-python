#!/usr/bin/env python3
"""duck-typed annotations"""
from typing import Union, Any


def safe_first_element(lst: list) -> Union[Any, None]:
    """returns first element of a list if exists, otherwise None"""
    if lst:
        return lst[0]
    return None
