#!/usr/bin/env python3
"""
    duck type and iteration
"""
from typing import Iterable, List, Union, Sequence, Tuple


def element_length(lst: Iterable[Sequence])\
        -> List[Tuple[Sequence, int]]:
    """
        Sequence of list
    """

    return [(i, len(i)) for i in lst]
