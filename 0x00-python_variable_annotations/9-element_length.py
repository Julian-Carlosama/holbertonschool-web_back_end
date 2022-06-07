#!/usr/bin/env python3
"""
    Module that return values with the appropriate types
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """  Return list of tuple of sequence of integers """
    return [(i, len(i)) for i in lst]
