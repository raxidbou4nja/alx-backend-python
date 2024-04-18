#!/usr/bin/env python3
"""
    6. mixed types - list of floats and ints
"""
from typing import List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Returns the sum of a list of floats & ints.
    """
    result: float = 0

    for x in mxd_lst:
        result += x

    return result
