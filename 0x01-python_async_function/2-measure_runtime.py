#!/usr/bin/env python3
""" Functions that measure the runtime """

import asyncio
from typing import List
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """ Return the random time """
    first_time = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    ended = time.perf_counter() - first_time
    total_time = ended / n

    return total_time
