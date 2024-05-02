#!/usr/bin/env python3
"""TypeVar module with annotations"""
from typing import Dict
from typing import TypeVar
from typing import Optional

KT = TypeVar('KT')
VT = TypeVar('VT')


def safely_get_value(dct: Dict[KT, VT], key: KT,
                     default: Optional[VT] = None) -> VT:
    """Return a value of a key in a dictionary"""
    if key in dct:
        return dct[key]
    return default
