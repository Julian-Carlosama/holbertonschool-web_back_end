#!/usr/bin/env python3
""" Asynchronous that takes in an int argument
    and return a random delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Return the random time """

    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
