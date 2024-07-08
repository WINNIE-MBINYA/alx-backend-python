#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random delay
between 0 and max_delay (included) seconds and eventually returns it.
"""
import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and
    max_delay seconds and returns the delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The actual delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
