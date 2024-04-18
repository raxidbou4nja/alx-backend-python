#!/usr/bin/env python3
"""
    callable function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        multiplier factor
    """

    def x(f: float) -> float:
        """ Get the second argument somthing like JS """
        return float(f * multiplier)

    return x
