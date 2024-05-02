#!/usr/bin/env python3
"""duck-typed annotations"""
from typing import Tuple, List, Union, Any


def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    """returns first element of a list if exists, otherwise None"""
    if lst:
        return lst[0]
    else:
        return None
