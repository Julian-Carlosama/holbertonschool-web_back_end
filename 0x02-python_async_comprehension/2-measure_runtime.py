#!/usr/bin/env python3
"""
    Coroutine that will execute async_comprehension 
    four times in parallel using asyncio.gather.
"""
import random
import asyncio
import time
from typing import Generator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:

    """
        Execute async_comprehension four times
        in parallel using asyncio.gather
    """
    start_task = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_task = time.time()
    total_time: float = end_task - start_task
    return total_time
