#!/usr/bin/env python3
"""Element length module"""
from typing import List, Tuple


def element_length(lst: List[str]) -> Tuple[int, List[int]]:
    """Returns a tuple with the length of a string and a list of lengths"""
    return (len(lst), [len(i) for i in lst])
