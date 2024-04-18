#!/usr/bin/env python3
"""
    duck typing typevar
"""
from typing import Mapping, TypeVar, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None)\
        -> Union[Any, T]:
    """
        dct: Mapping
        key: Any data type
        default: Default value

        return: any or T format
    """
    if key in dct:
        return dct[key]
    else:
        return default
