#!/usr/bin/env python3
"""
Module for to_kv function.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int/float and returns a tuple.
    The first element is the string,
    and the second element is the square of the int/float.
    """
    return (k, float(v**2))
