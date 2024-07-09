#!/usr/bin/env python3

import asyncio
import time
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the runtime of four async_comprehension
    coroutines running in parallel.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
