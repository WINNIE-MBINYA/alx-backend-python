#!/usr/bin/env python3
"""
This module contains a function that
measures the total execution time for wait_n(n, max_delay).
"""
import time
import asyncio
from typing import Union

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average time per wait_random call.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
