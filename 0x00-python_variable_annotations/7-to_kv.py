#!/usr/bin/env python3
"""Type-annotated function to_kv that takes a string
k and an int OR float v as arguments and returns a tuple
containing k and the square of v. The float v should be
annotated as a float and return a float. The annotation for v is str."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple containing k and the square of v"""
    return (k, v * v)
