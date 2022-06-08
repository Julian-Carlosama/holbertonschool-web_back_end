#!/usr/bin/env python3
"""
    Function that takes an integer max_delay
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Returns a asyncio task """
    return asyncio.create_task(wait_random(max_delay))
