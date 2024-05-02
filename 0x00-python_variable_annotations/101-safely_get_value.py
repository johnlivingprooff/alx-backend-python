#!/usr/bin/env python3
"""TypeVar module with annotations"""
from typing import Dict, Any
from typing import TypeVar
from typing import Union
from typing import Mapping


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'), None] = None
                     ) -> Union[Any, TypeVar("T")]:
    """Return a value of a key in a dictionary"""
    if key in dct:
        return dct[key]
    return default
