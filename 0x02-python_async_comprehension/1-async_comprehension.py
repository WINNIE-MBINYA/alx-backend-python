#!/usr/bin/env python3

import asyncio
from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator.
    """
    return [i async for i in async_generator()]
