#!/usr/bin/env python3
"""Element length module with annotations"""
from typing import List
from typing import Tuple
from typing import Sequence


def element_length(lst: List[str]) -> List[Tuple[Sequence, int]]:
    """Returns a tuple with the length of a string and a list of lengths"""
    return (len(lst), [len(i) for i in lst])
