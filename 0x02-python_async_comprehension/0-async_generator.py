#!/usr/bin/env python3

import asyncio
import random


async def async_generator():
    """
    Asynchronously yields random numbers between 0 and 10 with a 1-second delay
    between each yield.
    """

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
