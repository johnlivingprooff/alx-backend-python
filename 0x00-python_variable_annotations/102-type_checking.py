#!/usr/bin/env python3
"""Type Checking"""
from typing import Tuple, List, Any, Union


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a list of tuples"""
    zoomed_in: List[Tuple] = [
        (item * factor) for item in lst
    ]
    return zoomed_in
