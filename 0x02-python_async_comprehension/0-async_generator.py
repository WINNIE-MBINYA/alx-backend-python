#!/usr/bin/env python3

"""
Module containing the async_generator coroutine for yielding random numbers.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that loops 10 times, each time asynchronously waits 1 second,
    then yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
