#!/usr/bin/env python3
"""
Complex types - Functions (Returning Callables -)
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Write a type-annotated function make_multiplier
    that takes a float multiplier as argument and
    returns a function that multiplies a float by
    multiplier.
    """
    def float_multiply(x: float) -> float:
        return multiplier * x

    return float_multiply
