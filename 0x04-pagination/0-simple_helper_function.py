#!/usr/bin/env python3
"""
    Function that takes two integer arguments page and page_size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Function should return a tuple of size two containing a start index
        and an end index corresponding to the range of indexes to return in
        a list for those particular pagination parameters.
    """

    start = (page-1) * page_size
    end = page * page_size
    i_range = (start, end)
    return i_range
