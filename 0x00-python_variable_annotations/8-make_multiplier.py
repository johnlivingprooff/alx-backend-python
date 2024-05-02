#!/usr/bin/env python3
"""Float multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier"""
    def f_multiply(n: float) -> float:
        """Multiply a float by multiplier"""
        return n * multiplier
    return f_multiply
