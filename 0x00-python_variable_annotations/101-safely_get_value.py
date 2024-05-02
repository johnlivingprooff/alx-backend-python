#!/usr/bin/env python3
"""TypeVar module"""
from typing import TypeVar, Union, Any, Mapping


def safely_get_value(dct: Mapping, key: Any, default: Union[TypeVar('T'), None] = None) -> Union[Any, TypeVar('T')]:
    """Return a value of a key in a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
