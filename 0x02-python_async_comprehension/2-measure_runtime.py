#!/usr/bin/env python3

import asyncio
import time  # Import the time module for time measurement
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension four times
    in parallel using asyncio.gather.

    Explanation of the observed 10-second runtime:

    - While each individual call to async_comprehension might take roughly 1
      second due to the delays within the async generator, running them in
      parallel doesn't guarantee a combined runtime of 4 seconds.

    - Each coroutine execution still involves scheduling, context switching,
      and potential I/O operations, which contribute to the overall runtime.

    - asyncio aims to optimize for concurrency, not necessarily strict
      parallelization.
      It might interleave coroutines based on available resources
      and priorities.

    - Therefore, the observed runtime around 10 seconds reflects the combined
      execution time of the four coroutines, including scheduling overhead.
    """

    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()

    return end_time - start_time
